import pandas as pd
data = pd.read_csv("popular-text-channels.csv")

# 0_comment_ch = [name for name in data.channel_name[data.messages == 0]]
# un-comment to get new list of never typed in channels

safe_chan = ['official-judge-proof', 'rules', 'any-other-deck', 'roles', 'pro-player-chat', 'tournament-reports',
             'featured-decks-voting', 'modmail-log', 'top-100-global-proof', 'legend-anthology-decks',
             'xyz-festival-decks', '🔥xyz-5-winstreak-xyz-festival', '🔥submit-guides', 'welcome', 'Unknown',
             'content-creator-proof', 'mod-application', 'guide-submission', 'top-100-decklists', 'deck-directory',
             'organizers-channel', 'pro-player-proof', 'server-news', 'feedback-responses', 'tournament-organizer-proof',
             'master-duel-news', 'helper-handbook', 'tournament-discussion', 'reddit-discussion', 'management',
             'hidden-tips-and-info', 'share-player-id', 'shadow-realm', 'astera-bot-logs', 'ban-logs', 'ckrit', 'timeout-log',
             'carls-logs', 'join-and-leave', 'application-discussion', 'mee6-logs', 'judge-discussion', 'message-deleted',
             'mod-discussion', 'helper-application']

new_data = data.drop("interval_start_timestamp", axis=1)
new_data2 = new_data[~new_data["channel_name"].isin(safe_chan)]

fourm_threads = [chname for chname in data.channel_name if chname[0] != "'"]
diamond = [chname for chname in data.channel_name if "diamond" not in chname]

new_data3 = new_data2[new_data2.channel_name.isin(diamond)]
new_data3 = new_data3[new_data3.channel_name.isin(fourm_threads)]
x = 10
print(f"Low activity channels ({x} lowest channels by # of messages sent per month)")
messages_data = new_data3.nsmallest(x, "messages")
print(messages_data.to_string(index=False))
print("------------------------------------------------------------------------------")
print(f"Low viewership channels ({x} lowest channels by # of people who open and read channel per month)")
reader_data = new_data3.nsmallest(x, "readers")
print(reader_data.to_string(index=False))
print("------------------------------------------------------------------------------")
print(f"Low Chatters channels ({x} lowest channels by # of people who type in channel per month)")
chatter_data = new_data3.nsmallest(x, "chatters")
print(chatter_data.to_string(index=False))
print("------------------------------------------------------------------------------")

frames = [chatter_data, reader_data, messages_data]
combined_data = pd.concat(frames)

readers = []
chatters = []
messages = []

for ch in messages_data.channel_name:
    messages.append(ch)
for ch in reader_data.channel_name:
    readers.append(ch)
for ch in chatter_data.channel_name:
    chatters.append(ch)

matches = []
for channel in readers:
    if channel in chatters or channel in messages:
        matches.append(str(channel))

for channel in chatters:
    if channel in readers or channel in messages:
        matches.append(str(channel))

for word in matches:
    if matches.count(word) > 1:
        matches.remove(word)

ids = combined_data.channel_id[combined_data.channel_name.isin(matches)]
id_list = []
for id in ids:
    if id not in id_list:
        id_list.append(id)
    else:
        pass
print(f"{', '.join(matches)} are in multiple low activity lists")
link_list = []
for thing in id_list:
    link_list.append(f"<#{thing}>")
print("Copy paste channel hops:")
print(f"    {', '.join(link_list)}")

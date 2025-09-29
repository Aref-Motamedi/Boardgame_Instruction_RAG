import os

# Create documents directory
os.makedirs("documents", exist_ok=True)

# Create board game rule books
boardgame_rules = {
    "ticket_to_ride_rules.txt": """
TICKET TO RIDE - COMPLETE RULES AND INSTRUCTIONS

GAME OVERVIEW:
Ticket to Ride is a cross-country train adventure game for 2-5 players. Players collect cards of various types of train cars and use them to claim railway routes connecting cities throughout North America. The longer the routes, the more points they earn. Additional points come from fulfilling Destination Tickets – goal cards that connect distant cities – and from building the longest continuous route.

GAME COMPONENTS:
- 1 Board map of North American train routes
- 240 Colored Train Cars (45 each in Blue, Red, Green, Yellow, Black, and 20 multi-colored)
- 110 Train Car cards (12 of each color, plus 14 Locomotive wild cards)
- 30 Destination Ticket cards
- 5 Wooden Scoring Markers (one per player color)
- 1 Summary card for each player
- 1 Longest Route Bonus card worth 10 points

SETUP:
1. Place the board map in the center of the table.
2. Each player takes a set of 45 Colored Train Cars and places their Scoring Marker on Start (space 0) of the scoring track.
3. Shuffle the Train Car cards and deal 4 cards to each player. Place the deck face-down near the board and turn the top 5 cards face-up next to it.
4. Shuffle the Destination Ticket cards and deal 3 cards to each player. Each player must keep at least 2 tickets but may keep all 3. Place remaining tickets face-down near the board.
5. The player who has visited the most American states (or territories) goes first.

HOW TO PLAY:
On their turn, a player must perform ONE of these actions:

ACTION 1 - DRAW TRAIN CAR CARDS:
The player may draw 2 Train Car cards. They may take any of the 5 face-up cards or draw from the top of the deck (blind draw). If taking a face-up card, immediately replace it with a new card from the deck. 
SPECIAL RULE: Locomotive cards are wild and can represent any color. If a player takes a face-up Locomotive, that is their only card draw for that turn. However, if drawing blind from the deck and getting a Locomotive, they may still draw their second card.
If at any time, 3 of the 5 face-up cards are Locomotives, immediately discard all 5 cards and replace them with new ones.

ACTION 2 - CLAIM A ROUTE:
To claim a route, a player must play a set of Train Car cards equal to the number of spaces in that route. The cards must match the color of the route (or use Locomotives as wild cards). For gray routes, any single color may be used.
After playing the cards, place your colored trains on each space of that route and score points immediately:
- 1 space = 1 point
- 2 spaces = 2 points
- 3 spaces = 4 points
- 4 spaces = 7 points
- 5 spaces = 10 points
- 6 spaces = 15 points
- 8 spaces = 21 points (found only in the 1910 expansion)

DOUBLE ROUTES: Some cities are connected by Double Routes (two parallel routes). Important rules:
- In 2-3 player games, only one of the two routes can be claimed.
- In 4-5 player games, both routes can be claimed, but not by the same player.

ACTION 3 - DRAW DESTINATION TICKET CARDS:
The player draws 3 Destination Ticket cards from the top of the deck. They must keep at least one but may keep two or all three. Any cards not kept are placed at the bottom of the deck.

DESTINATION TICKETS:
Each Destination Ticket shows two cities and a point value. If the cities are connected by a continuous path of your trains at the end of the game, you score the points shown. If not connected, you LOSE those points. Keep your Destination Tickets secret until the end of the game.

END OF GAME:
The game ends when any player has 2 or fewer train cars left at the end of their turn. Each player (including the player who triggered the end) gets one final turn, then the game ends and final scoring begins.

FINAL SCORING:
1. Players reveal all their Destination Tickets.
2. Add points for completed Destination Tickets.
3. Subtract points for incomplete Destination Tickets.
4. The player with the Longest Continuous Route receives the 10-point bonus card. A continuous path may include loops and pass through the same city multiple times, but no route may be used twice. In case of a tie, all tied players receive 10 points.
5. The player with the most points wins! In case of a tie, the player who completed the most Destination Tickets wins. If still tied, the player with the Longest Route bonus wins.

STRATEGY TIPS:
- Claim longer routes early as they give better point-per-card ratios.
- Don't draw too many Destination Tickets unless you're confident you can complete them.
- Watch what routes your opponents might need and consider blocking them.
- Keep some Locomotives in hand as they provide flexibility.
- Try to build routes that satisfy multiple Destination Tickets simultaneously.
- The Longest Route bonus can be game-changing – aim for 10+ connected routes if possible.

VARIANTS FOR ADVANCED PLAYERS:
- "Big Cities" variant: Deal 4 Destination Tickets to each player at the start. Players must keep at least 3.
- "Megalopolis" variant: Players receive 1 bonus point for every ticket completed, regardless of the ticket's point value.
""",

    "the_crew_rules.txt": """
THE CREW: QUEST FOR PLANET NINE - COMPLETE RULES AND INSTRUCTIONS

GAME OVERVIEW:
The Crew is a cooperative trick-taking card game for 2-5 players. Players work together as astronauts on a space mission to find the mysterious Planet Nine. The game consists of 50 missions with increasing difficulty. Players must win specific tricks containing certain cards, but communication is severely limited!

GAME COMPONENTS:
- 40 Game cards (numbered 1-9 in four colors: Pink, Blue, Green, Yellow, plus four special Rocket cards numbered 1-4)
- 36 Task cards (showing which cards must be won)
- 16 Tokens (5 arrow tokens, 5 reminder tokens, 5 communication tokens, 1 commander token)
- 1 Mission logbook with 50 missions
- 5 large task overview cards (one per player)

CARD HIERARCHY:
In each of the four colored suits (Pink, Blue, Green, Yellow), cards are ranked 1 (lowest) to 9 (highest).
Rocket cards are TRUMP cards and always beat colored cards. Rockets rank 1 (lowest) to 4 (highest).

SETUP:
1. Choose a mission from the logbook. Each mission specifies how many task cards to use and any special rules.
2. Shuffle the 40 game cards and deal them evenly to all players. In 3-player games, remove all cards numbered 1-3 from the deck before dealing. In 4-player games, each player gets 10 cards. In 5-player games, each player gets 8 cards.
3. The player who receives the Rocket 4 card becomes the Commander and takes the Commander token.
4. Place the specified number of task cards face-up in the center of the table.
5. Give each player a task overview card for reference.

DISTRIBUTING TASKS:
The Commander chooses one task card from the center and places it in front of any player (including themselves). Then, proceeding clockwise, each player chooses a task card and assigns it to any player. Continue until all task cards are distributed.
IMPORTANT: Each player must win the tricks containing the cards shown on their assigned task cards.

MISSION REQUIREMENTS:
Some missions have special requirements shown with tokens placed on task cards:
- NUMBERED TOKENS (1, 2, 3, etc.): Tasks must be completed in the specified order. Place these tokens on task cards to show the sequence.
- ARROW TOKEN (>): The task with this token must be completed BEFORE the next task.
- OMEGA TOKEN (Ω): The task with this token must be completed LAST, after all other tasks.

HOW TO PLAY - TRICK-TAKING RULES:
The Commander leads the first trick by playing any card from their hand. Going clockwise, each player must:
1. FOLLOW SUIT if possible (play a card of the same color as the led card).
2. If unable to follow suit, play any card (including a Trump/Rocket card).

WINNING A TRICK:
- The highest card of the led suit wins the trick UNLESS a Trump/Rocket was played.
- If one or more Trump/Rocket cards were played, the highest Trump/Rocket wins.
- The winner of the trick leads the next trick.

When a trick is won, check if it contains a card shown on any player's task card:
- If the player who won the trick has that task card in front of them, they have completed that task! Turn the task card face-down.
- If the player who won the trick does NOT have that task card, the mission is FAILED immediately.

COMMUNICATION RULES:
Communication is STRICTLY LIMITED. Players cannot discuss strategy, hint about their cards, or show reactions. HOWEVER, once per mission, each player may use their communication token:

1. Place your communication token on any card in your hand.
2. Depending on where you place the token, you communicate:
   - Token on TOP of card = "This is my HIGHEST card in this color"
   - Token on BOTTOM of card = "This is my LOWEST card in this color"  
   - Token in MIDDLE of card = "This is my ONLY card in this color"

RESTRICTIONS on communication:
- You can only communicate once per mission.
- Once you've communicated, you cannot take back or change your communication.
- You cannot communicate about Trump/Rocket cards.
- The Commander must wait until all players have played one card in the first trick before communicating.
- After communication, other players may now communicate on their turns.

RADIO COMMUNICATION (available in some missions):
Some missions show a radio symbol. In these missions, players may briefly discuss before distributing tasks. The Commander decides when discussion ends. Once tasks are distributed, normal communication rules apply.

DISTRESS SIGNAL:
If the mission seems impossible to complete, any player may call a "Distress Signal" to abort the mission and try again. However, this counts as a failed attempt. After 3 failed attempts (including Distress Signals), you may skip that mission and move to the next one.

WINNING AND LOSING:
MISSION SUCCESS: You win the mission when all task cards are completed (face-down) and all tricks have been played.
MISSION FAILURE: The mission fails immediately if:
- A player wins a trick containing a card from another player's task card
- A task is completed out of order (when numbered tokens are used)
- All tricks are played but not all tasks are completed

After completing a mission, move to the next mission in the logbook. The goal is to complete all 50 missions!

VARIANTS FOR DIFFERENT PLAYER COUNTS:
2-PLAYER VARIANT: Use only cards 5-9 in each color plus all Rockets. Deal 10 cards to each player. Play is simultaneous – both players play a card, the higher card wins.

3-PLAYER VARIANT: Remove cards 1-3 before dealing. Adjust task card numbers as specified in mission logbook.

STRATEGY TIPS:
- Use communication wisely! Save it for critical moments.
- Pay attention to what others communicate – it reveals important information.
- The Commander should carefully observe all players before making decisions.
- When distributing tasks, consider who is likely to win certain tricks based on their position.
- Sometimes winning a trick early is important; other times, you want to lose tricks.
- Trump/Rocket cards are powerful but should be used strategically.
- In later missions with multiple tokens, plan the sequence carefully.

ADVANCED STRATEGY:
- Card counting is essential – remember what's been played.
- The player after the Commander has an advantage as they see the led card before playing.
- Sometimes it's strategic to take a task card that seems difficult to prevent others from getting stuck with it.
- Use low cards early to clear suits so you can play freely later.
""",

    "coup_rules.txt": """
COUP - COMPLETE RULES AND INSTRUCTIONS

GAME OVERVIEW:
Coup is a bluffing and deduction game for 2-6 players set in a dystopian future. You are head of a family in an Italian city-state controlled by a weak government. You must manipulate, bluff, and bribe your way to power. Your goal is to be the last player with influence remaining. You start with two influence (represented by two character cards) and two coins. Through extortion, assassination, and deception, you eliminate your opponents' influence while protecting your own.

GAME COMPONENTS:
- 15 Character cards (3 each of Duke, Assassin, Captain, Ambassador, Contessa)
- 50 Coin tokens
- 6 Summary cards (one per player)

THE FIVE CHARACTERS AND THEIR POWERS:
1. DUKE: Take 3 coins from the Treasury (Tax). Block someone from taking Foreign Aid.
2. ASSASSIN: Pay 3 coins to assassinate another player's influence.
3. CAPTAIN: Take 2 coins from another player (Steal). Block someone from stealing from you.
4. AMBASSADOR: Draw 2 cards from the deck, choose which (if any) to keep, and return 2 cards to the deck. Block someone from stealing from you.
5. CONTESSA: Block an assassination attempt against you.

SETUP:
1. Shuffle the 15 character cards and deal 2 cards face-down to each player. These are your "influence" – look at them secretly but don't reveal them to other players.
2. Place remaining cards face-down in the center as the Court deck.
3. Give 2 coins to each player from the Treasury.
4. Place remaining coins in the center as the Treasury.
5. Each player takes a summary card for reference.
6. Choose a starting player randomly.

YOUR INFLUENCE:
Your two character cards represent your influence in the game. Keep them face-down in front of you. When you lose influence, you must choose one card to reveal and turn face-up. Once revealed, that character's power is permanently lost to you. If you lose both influences, you are eliminated from the game.

HOW TO PLAY:
On your turn, you MUST take one action. There are two types of actions:

GENERAL ACTIONS (always available to everyone):
1. INCOME: Take 1 coin from the Treasury. (Cannot be challenged or blocked)
2. FOREIGN AID: Take 2 coins from the Treasury. (Cannot be challenged, but can be blocked by Duke)
3. COUP: Pay 7 coins to the Treasury and launch a Coup against another player. That player loses an influence of their choice. (Cannot be challenged or blocked)

CHARACTER ACTIONS (require claiming a character):
4. TAX (Duke): Take 3 coins from the Treasury.
5. ASSASSINATE (Assassin): Pay 3 coins to the Treasury and assassinate another player's influence.
6. STEAL (Captain): Take 2 coins from another player.
7. EXCHANGE (Ambassador): Draw 2 cards from the Court deck, look at them, choose which cards to keep (you may keep 0, 1, or 2), then return cards until you have 2 total. Shuffle and return excess cards to the Court deck.

MANDATORY ACTION:
If you start your turn with 10 or more coins, you MUST launch a Coup. You cannot take any other action.

CHALLENGING:
When a player claims a character action (Tax, Assassinate, Steal, or Exchange), any other player may challenge them. If challenged:
1. The challenged player must prove they have that character by revealing the card.
2. If they DO have the character: The challenger loses an influence of their choice. The challenged player shuffles their revealed card back into the Court deck and draws a new card.
3. If they DON'T have the character: The challenged player loses an influence. The action fails.

Only ONE player needs to challenge. If multiple players want to challenge, the player whose turn comes next (clockwise from the acting player) gets priority.

BLOCKING:
Certain actions can be blocked by claiming specific characters:

BLOCKABLE ACTIONS:
- FOREIGN AID can be blocked by claiming Duke
- STEALING can be blocked by claiming Captain OR Ambassador (only by the target)
- ASSASSINATION can be blocked by claiming Contessa (only by the target)

When blocking:
1. The blocking player claims to have the blocking character.
2. The original action is cancelled if the block stands.
3. The acting player (or any other player) may challenge the block.

CHALLENGE SEQUENCE:
If a block is challenged:
1. The blocker must prove they have that character by revealing it.
2. If they DO have the character: The challenger loses an influence. The blocker shuffles their revealed card back and draws a new card. The block succeeds.
3. If they DON'T have the character: The blocker loses an influence. The original action proceeds.

IMPORTANT TIMING RULE:
Challenges must be made immediately after the action or block is declared, before the action resolves. Once coins change hands or cards are drawn, it's too late to challenge.

LOSING INFLUENCE:
When you lose influence, YOU choose which of your face-down cards to reveal and turn face-up. Once face-up, you can no longer claim that character's power. If both your cards are face-up, you are eliminated from the game.

WINNING THE GAME:
The last player with at least one face-down influence remaining wins the game!

BLUFFING:
This is the heart of Coup! You can claim ANY character action, even if you don't have that character card. If no one challenges you, your action succeeds. But if someone challenges you and you're bluffing, you lose an influence and the action fails.

Similarly, you can claim to block with any character, even if you don't have it. The risk is being challenged.

STRATEGY TIPS:
- Early game: Focus on building coins with Income, Foreign Aid, and Tax.
- Assassinations are powerful but expensive. Consider whether challenging suspicious claims is worth the risk.
- If you have 7+ coins, other players know you can Coup next turn, making you a threat.
- Bluffing the Duke for Tax is common and often goes unchallenged early.
- The Contessa is crucial for defense but rare – bluffing Contessa blocks is risky but sometimes necessary.
- Track revealed cards. If all 3 Dukes are face-up, anyone claiming Duke is definitely bluffing!
- Sometimes revealing a card voluntarily when challenged is strategic – you draw a fresh card.
- Assassin + Contessa is a strong combo. Captain + Ambassador gives stealing and defense.

ADVANCED TACTICS:
- Count coins carefully. If someone has 8 coins, they can Assassinate then Coup next turn.
- Build alliances early, but be ready to betray when necessary.
- If you hold both of one character, you can safely claim it knowing you can't be proven wrong.
- Sometimes taking a challenge loss is worth it if your bluff worked multiple times before.
- Target players with one influence remaining – they're one Coup away from elimination.
- Don't hoard coins. Once you pass 7, you become the biggest threat at the table.

2-PLAYER VARIANT:
In 2-player games, each player starts with 1 influence (1 card) instead of 2. First player to eliminate their opponent's single influence wins. All other rules remain the same.

TEAM VARIANT (4 or 6 players):
Play in teams of 2. Teammates sit across from each other. You cannot target your teammate with harmful actions. First team to eliminate both opponents wins. You may not look at your teammate's cards or discuss strategy explicitly, but you can make implications through your actions.

INQUISITOR VARIANT (advanced):
Replace the Ambassador with the Inquisitor. The Inquisitor has these powers:
- Draw 1 card from the Court deck, choose whether to keep it or return it.
- Choose another player. Look at one of their cards (randomly). You may force them to exchange it with the Court deck.
- Block stealing (same as Ambassador).
""",
}

# Write the files
for filename, content in boardgame_rules.items():
    with open(f"documents/{filename}", "w", encoding="utf-8") as f:
        f.write(content.strip())

print("✅ Created 3 board game rule books:")
print("   - Ticket to Ride")
print("   - The Crew: Quest for Planet Nine")
print("   - Coup")
print("\nFiles saved in ./documents/")
print("\nYou can now ask questions like:")
print("   - 'How do you win in Ticket to Ride?'")
print("   - 'What are the communication rules in The Crew?'")
print("   - 'Can you block an assassination in Coup?'")
print("   - 'How many players can play Ticket to Ride?'")
#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "7D0922D1-D8E8-461D-A92C-7BD8B48D3F5D",
  "name": "Zork",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1630598168477,
  "passages": [
    {
      "name": "West of House",
      "tags": "",
      "id": "1",
      "text": "This is an open field west of a white house, with a boarded front door.\n\n[[NORTH->North of House]]\n[[SOUTH->South of House]]\n[[WEST->Forest]].",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of House",
          "original": "[[NORTH->North of House]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of House",
          "original": "[[SOUTH->South of House]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Forest",
          "original": "[[WEST->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is an open field west of a white house, with a boarded front door.\n\n\n\n."
    },
    {
      "name": "North of House",
      "tags": "",
      "id": "2",
      "text": "You are facing the north side of a white house.  There is no door here, and all the windows are barred.\n[[WEST->West of House]]\n[[EAST->East of House]]\n[[NORTH->Forest]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "West of House",
          "original": "[[WEST->West of House]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East of House",
          "original": "[[EAST->East of House]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "Forest",
          "original": "[[NORTH->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are facing the north side of a white house.  There is no door here, and all the windows are barred."
    },
    {
      "name": "South of House",
      "tags": "",
      "id": "3",
      "text": "You are facing the south side of a white house. There is no door here, and all the windows are barred.\n[[WEST->West of House]]\n[[EAST->East of House]]\n[[SOUTH->Forest]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "West of House",
          "original": "[[WEST->West of House]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East of House",
          "original": "[[EAST->East of House]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Forest",
          "original": "[[SOUTH->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are facing the south side of a white house. There is no door here, and all the windows are barred."
    },
    {
      "name": "Forest",
      "tags": "",
      "id": "4",
      "text": "This is a forest, with trees in all directions around you.\n[[NORTH->Sunlit Forest]]\n[[EAST->Forest]]\n[[SOUTH->Forest]]\n[[WEST->Forest]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Sunlit Forest",
          "original": "[[NORTH->Sunlit Forest]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Forest",
          "original": "[[EAST->Forest]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Forest",
          "original": "[[SOUTH->Forest]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Forest",
          "original": "[[WEST->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is a forest, with trees in all directions around you."
    },
    {
      "name": "East of House",
      "tags": "",
      "id": "5",
      "text": "You are behind the white house. A path leads into the forest to the east. In one corner of the house there is a small window which is slightly ajar.\n[[NORTH->North of House]]\n[[SOUTH->South of House]]\n[[EAST->Sunlit Forest]]\n[[WEST->Kitchen]]\n[[ENTER->Kitchen]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of House",
          "original": "[[NORTH->North of House]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of House",
          "original": "[[SOUTH->South of House]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Sunlit Forest",
          "original": "[[EAST->Sunlit Forest]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Kitchen",
          "original": "[[WEST->Kitchen]]"
        },
        {
          "linkText": "ENTER",
          "passageName": "Kitchen",
          "original": "[[ENTER->Kitchen]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are behind the white house. A path leads into the forest to the east. In one corner of the house there is a small window which is slightly ajar."
    },
    {
      "name": "Sunlit Forest",
      "tags": "",
      "id": "6",
      "text": "his is a dimly lit forest, with large trees all around.  One particularly large tree with some low branches stands here.\n[[NORTH->Forest]]\n[[SOUTH->Forest]]\n[[EAST->Forest]]\n[[WEST->East of House]]\n[[UP->Tree]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Forest",
          "original": "[[NORTH->Forest]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Forest",
          "original": "[[SOUTH->Forest]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Forest",
          "original": "[[EAST->Forest]]"
        },
        {
          "linkText": "WEST",
          "passageName": "East of House",
          "original": "[[WEST->East of House]]"
        },
        {
          "linkText": "UP",
          "passageName": "Tree",
          "original": "[[UP->Tree]]"
        }
      ],
      "hooks": [],
      "cleanText": "his is a dimly lit forest, with large trees all around.  One particularly large tree with some low branches stands here."
    },
    {
      "name": "Kitchen",
      "tags": "",
      "id": "7",
      "text": "You are in the kitchen of the white house. A table seems to have been used recently for the preparation of food. A passage leads to the west and a dark staircase can be seen leading upward. A dark chimney leads down and to the east is a small window which is open.\n[[EAST->East of House]]\n[[Upward->Upstairs]]\n[[Down -> Dark Chimney]]",
      "links": [
        {
          "linkText": "EAST",
          "passageName": "East of House",
          "original": "[[EAST->East of House]]"
        },
        {
          "linkText": "Upward",
          "passageName": "Upstairs",
          "original": "[[Upward->Upstairs]]"
        },
        {
          "linkText": "Down",
          "passageName": "Dark Chimney",
          "original": "[[Down -> Dark Chimney]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are in the kitchen of the white house. A table seems to have been used recently for the preparation of food. A passage leads to the west and a dark staircase can be seen leading upward. A dark chimney leads down and to the east is a small window which is open."
    },
    {
      "name": "Tree",
      "tags": "",
      "id": "8",
      "text": "You are about 10 feet above the ground nestled among some large branches. The nearest branch above you is above your reach. Beside you on the branch is a small bird's nest.\n[[DOWN->Sunlit Forest]]",
      "links": [
        {
          "linkText": "DOWN",
          "passageName": "Sunlit Forest",
          "original": "[[DOWN->Sunlit Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are about 10 feet above the ground nestled among some large branches. The nearest branch above you is above your reach. Beside you on the branch is a small bird's nest."
    },
    {
      "name": "Upstairs",
      "tags": "",
      "id": "9",
      "text": "Following the staircase, you begin to climb, each step creaking loudly, breaking the unnatural silence of the house. At the top of the Stairs, a dark hallway greets you with silence. In front of you lie 3 doors. One on your left, one on the right, and one at the end of the hall. All of the doors are locked\n[[Back->Kitchen]]",
      "links": [
        {
          "linkText": "Back",
          "passageName": "Kitchen",
          "original": "[[Back->Kitchen]]"
        }
      ],
      "hooks": [],
      "cleanText": "Following the staircase, you begin to climb, each step creaking loudly, breaking the unnatural silence of the house. At the top of the Stairs, a dark hallway greets you with silence. In front of you lie 3 doors. One on your left, one on the right, and one at the end of the hall. All of the doors are locked"
    },
    {
      "name": " Dark Chimney",
      "tags": "",
      "id": "10",
      "text": "As you walk down from the kitchen, you find yourself in the living room of the house. The old furniture is nearly rotting at this point, and the scent of mold overwhelms your senses. You are drawn to the fireplace, where you notice that the brick inside is stained dark with ash. As you investigate you notice a small hatch at the back of the chimney.\n[[Open-> Hatch]]\n[[Back ->Kitchen]]",
      "links": [
        {
          "linkText": "Open",
          "passageName": "Hatch",
          "original": "[[Open-> Hatch]]"
        },
        {
          "linkText": "Back",
          "passageName": "Kitchen",
          "original": "[[Back ->Kitchen]]"
        }
      ],
      "hooks": [],
      "cleanText": "As you walk down from the kitchen, you find yourself in the living room of the house. The old furniture is nearly rotting at this point, and the scent of mold overwhelms your senses. You are drawn to the fireplace, where you notice that the brick inside is stained dark with ash. As you investigate you notice a small hatch at the back of the chimney."
    },
    {
      "name": " Hatch",
      "tags": "",
      "id": "11",
      "text": "After opening the hatch, you notice a ladder leading into the depths of the house. The bottom is too dark to see, and the stench of decay begins to waft upwards into the living room.\n[[Back->Kitchen]] \n[[Down->Hidden Cellar]]",
      "links": [
        {
          "linkText": "Back",
          "passageName": "Kitchen",
          "original": "[[Back->Kitchen]]"
        },
        {
          "linkText": "Down",
          "passageName": "Hidden Cellar",
          "original": "[[Down->Hidden Cellar]]"
        }
      ],
      "hooks": [],
      "cleanText": "After opening the hatch, you notice a ladder leading into the depths of the house. The bottom is too dark to see, and the stench of decay begins to waft upwards into the living room."
    },
    {
      "name": "Hidden Cellar",
      "tags": "",
      "id": "12",
      "text": "The ladder is old and rickety, each step feels like it could be your last. As you reach the bottom, you come across an iron door, with a sliver of cold light creeping around its sillouette.\n[[Enter->Shelter]]\n[[Back->Too Late]]",
      "links": [
        {
          "linkText": "Enter",
          "passageName": "Shelter",
          "original": "[[Enter->Shelter]]"
        },
        {
          "linkText": "Back",
          "passageName": "Too Late",
          "original": "[[Back->Too Late]]"
        }
      ],
      "hooks": [],
      "cleanText": "The ladder is old and rickety, each step feels like it could be your last. As you reach the bottom, you come across an iron door, with a sliver of cold light creeping around its sillouette."
    },
    {
      "name": "Shelter",
      "tags": "",
      "id": "13",
      "text": "As you Open the door, you find what you've been looking for. Your targets are in front of you, the family you've been sent to eliminate. The man you presume is the father, was wounded by you last week, and his wound has begun to fester. As you enter the room, you know what you must do.\n[[Finish The Job -> Ending 1]]\n[[Resist -> Ending 2]]",
      "links": [
        {
          "linkText": "Finish The Job",
          "passageName": "Ending 1",
          "original": "[[Finish The Job -> Ending 1]]"
        },
        {
          "linkText": "Resist",
          "passageName": "Ending 2",
          "original": "[[Resist -> Ending 2]]"
        }
      ],
      "hooks": [],
      "cleanText": "As you Open the door, you find what you've been looking for. Your targets are in front of you, the family you've been sent to eliminate. The man you presume is the father, was wounded by you last week, and his wound has begun to fester. As you enter the room, you know what you must do."
    },
    {
      "name": "Too Late",
      "tags": "",
      "id": "14",
      "text": "As you attempt to turn back, something within you compels you to open the door. A savage instinct within you urges you to move forward. \"Finish your task\" a voice in your head orders you.\n[[Open->Shelter]] \n[[Resist->Finish it]]",
      "links": [
        {
          "linkText": "Open",
          "passageName": "Shelter",
          "original": "[[Open->Shelter]]"
        },
        {
          "linkText": "Resist",
          "passageName": "Finish it",
          "original": "[[Resist->Finish it]]"
        }
      ],
      "hooks": [],
      "cleanText": "As you attempt to turn back, something within you compels you to open the door. A savage instinct within you urges you to move forward. \"Finish your task\" a voice in your head orders you."
    },
    {
      "name": "Finish it",
      "tags": "",
      "id": "15",
      "text": "As you resist the voice in your head yells, \"YOU MUST OBEY THE ORDER\"\n[[Resist->Ending 3]]\n[[Obey->Shelter]]",
      "links": [
        {
          "linkText": "Resist",
          "passageName": "Ending 3",
          "original": "[[Resist->Ending 3]]"
        },
        {
          "linkText": "Obey",
          "passageName": "Shelter",
          "original": "[[Obey->Shelter]]"
        }
      ],
      "hooks": [],
      "cleanText": "As you resist the voice in your head yells, \"YOU MUST OBEY THE ORDER\""
    },
    {
      "name": " Ending 1",
      "tags": "",
      "id": "16",
      "text": "You raise your rifle and open fire. Blood splatters across the wall, as gunshots reverberate in the small room. Your ears ring with pain, and your cold heart feels no remorse. You cannot allow feelings of guilt to seep into your duty. As the family lies dead, you contact your superiors to let them know. A clean up crew is on the way. And you have to get ready for the next job.\nThe End.",
      "links": [],
      "hooks": [],
      "cleanText": "You raise your rifle and open fire. Blood splatters across the wall, as gunshots reverberate in the small room. Your ears ring with pain, and your cold heart feels no remorse. You cannot allow feelings of guilt to seep into your duty. As the family lies dead, you contact your superiors to let them know. A clean up crew is on the way. And you have to get ready for the next job.\nThe End."
    },
    {
      "name": " Ending 2",
      "tags": "",
      "id": "17",
      "text": "You hesitate as you look at the family in front of you, and in that moment, you hear a loud bang. For a moment, you feel a brief pain, then something wet trickles down your forehead. You catch a glimpse of a young child holding a gun across the room. Everything goes dark.\nThe End",
      "links": [],
      "hooks": [],
      "cleanText": "You hesitate as you look at the family in front of you, and in that moment, you hear a loud bang. For a moment, you feel a brief pain, then something wet trickles down your forehead. You catch a glimpse of a young child holding a gun across the room. Everything goes dark.\nThe End"
    },
    {
      "name": "Ending 3",
      "tags": "",
      "id": "18",
      "text": "You begin climbing up the ladder, you find yourself back in the living room, and you push through the kithcen. The whole time, orders are being directed at you, but you ignore them. Having gone rogue, you take out the earpiece, and throw down your rifle. You will have to live your life on the run from now on. A powerful force has decided your fate, and a sense of relief washes over you. \nThe End.",
      "links": [],
      "hooks": [],
      "cleanText": "You begin climbing up the ladder, you find yourself back in the living room, and you push through the kithcen. The whole time, orders are being directed at you, but you ignore them. Having gone rogue, you take out the earpiece, and throw down your rifle. You will have to live your life on the run from now on. A powerful force has decided your fate, and a sense of relief washes over you. \nThe End."
    }
  ]
}

if "name" in world and "passages" in world:
    print(world["name"])
    print()
    for passage in world["passages"]:
        print(passage["name"])
        print(passage["cleanText"])
        for link in passage["links"]:
            print(link["linkText"])
        print()
# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1

scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

# scorers
scorers = scorer_0 + ' ' + str(goal_0) + ', ' + scorer_1 + ' ' + str(goal_1)
print(scorers,'\n')

# report
report = f'{scorer_0} scored in the {str(goal_0)}nd minute\n{scorer_1} scored in the {str(goal_1)}th minute'
print(report,'\n')

# Part 2

# player
player = 'Marco van Basten'
print(player,'\n')

# first name
first_name = player[:player.find(' ')]
print(first_name,'\n')

# last name length
last_name_len = len(player[player.find(' ') + 1:])
print(last_name_len,'\n')

# short name
name_short = player[:1] + '.' + player[player.find(' '):]
print(name_short,'\n')

# chant
chant = ((first_name + '! ') * (len(player[:player.find(' ')]) - 1) + first_name + '!')
print(chant,'\n')

# good chant
good_chant = (chant[-1] != ' ')
print(good_chant,'\n')

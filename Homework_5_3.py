tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
if len(tutors) < len(klasses):
    tutors.append('None')
if len(tutors) > len(klasses):
    klasses.append('None')
my_zip = zip(tutors, klasses)
print(next(my_zip))
# from itertools import zip_longest
# my_gen = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses))
# print(next(my_gen))


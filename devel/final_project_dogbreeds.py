print ('Welcome')
name = input('What is your name? ')
print ('Hello ' + name + ', awnser a few simple yes or no questions to see what type of dogs it will suit your lifestyle')

one = input ('Do you like dogs? ')

two = input ('Have you ever owned a dog? ')

three = input ('Do you live in an apartment? ')

four = input ('Do you excercise regularly? ')

five = input ('Do you have time to walk/play with a dog? ')

six = input ('Do you have a dogpark near where you live? ')

seven = input ('Are you 20 or older? ')

eight = input ('Would you let a dog sleep in your bed? ')

nine = input ('Do you want a low maintenase dog? ')

ten = input ('Are you looking for a cuddle buddy? ')


if one and two and four and five and six == 'yes':
    print ('You would be the perfect owner for a medium to large sized dog, '+ name +'!')
    print ('Here are some breeds that will suit you')
    print ('Retrievers (labrador or goldens), Huskies, Beagles, German Sheperds, Spaniels, Basset Hounds')
    print ('Always remember, visit your local shelter and adopt a dog.')
    
elif one and two and four and five and six and seven and eight and nine and ten == 'yes':
    print ('The best dog for you would be a small dog')
    print ('Here are some dogs that will suit your lifestyle.')
    print ('Dachshunds, Chihuahuas, French Bulldogs, Beagles, Basset Hounds, Chitzus')
    
elif four and six == 'no':
    print ('The best dog for, '+ name+ ', you would be a small to medium sized dog')
    print ('Here are some dogs you should consider.')
    print ('Chihuahua, Chinese Crested, French Bulldog, Yorkshire Terrier, Pomerian, Dachshund')
    print ('Always remember, visit your local shelter and adopt a dog.')

else one == 'no':
    print ('If you do not like dogs but you want a pet you should adopt a cat or other animals.')
    print ('Always remember, visit your local shelter and adopt a pet.')


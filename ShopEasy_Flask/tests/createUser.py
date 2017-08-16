from user import User

peter = User('pktahinduka', 'Peter', 'Tahinduka', 'petertahinduka@gmail.com', 'jean')
paul = User('apaul', 'Paul', 'Ampuriire', 'paulampuriire@gmail.com', 'paul')
jean = User('jasiimwe', 'Jean', 'Asiimwe', 'jeanasiimwe@gmail.com', 'ajean')
moses = User('amoses', 'Moses', 'Akatwijuka', 'mosesakatwijuka@gmail.com', 'amoses')
racheal = User('akracheal', 'Racheal', 'Akatwijuka', 'akracheal@gmail.com', 'aracheal')

allUsers = [peter, paul, jean, moses, racheal]

for eachUser in allUsers:
    print(eachUser.firstName.split()[-1], eachUser.lastName, eachUser.email, eachUser.userName)
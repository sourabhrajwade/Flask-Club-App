from basic import db, Club, Privacy

## CREATE CLUB

club_pita = Club('Pita', 'Save animals', 'Rescue')
club_soccer =  Club('Yeta', 'Sports club india', 'Soccer')

db.session.add_all([club_pita, club_soccer])

## READ
all_club = Club.query.all()
print(all_club)

## SELECT BY ID
club_first = Club.query.get(1)
print(club_first)

## FILTER
club_soccer = Club.query.filter_by(categories='Soccer')
print(club_soccer.all())

### CREATE PRIVACY
privateF = Privacy(True, club_pita.id)

db.session.add(privateF)
db.session.commit()

## GRAB club_pita
club_soccer = Club.query.filter_by(categories='Rescue').first()
print(club_soccer)
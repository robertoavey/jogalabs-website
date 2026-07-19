#!/usr/bin/env python3
# Build usa_futsal_directory.json — seed data researched Jul 19 2026.
# Sources: usyouthfutsal.com/league-directory, usyouthfutsal.com/regional-championships,
# futsal.com, unitedfutsal.com, nationalfutsalpremierleague.com, en.wikipedia.org/wiki/National_Futsal_Premier_League
import io, os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))

REGION = {
 'WA':'West','OR':'West','CA':'West','NV':'West','ID':'West','MT':'West','WY':'West','UT':'West','CO':'West','AK':'West','HI':'West',
 'AZ':'Southwest','NM':'Southwest','TX':'Southwest','OK':'Southwest',
 'ND':'Midwest','SD':'Midwest','NE':'Midwest','KS':'Midwest','MN':'Midwest','IA':'Midwest','MO':'Midwest','WI':'Midwest','IL':'Midwest','IN':'Midwest','MI':'Midwest','OH':'Midwest',
 'AR':'South','LA':'South','MS':'South','AL':'South','TN':'South','KY':'South',
 'FL':'Southeast','GA':'Southeast','SC':'Southeast','NC':'Southeast',
 'VA':'Mid-Atlantic','WV':'Mid-Atlantic','MD':'Mid-Atlantic','DE':'Mid-Atlantic','DC':'Mid-Atlantic','PA':'Mid-Atlantic','NJ':'Mid-Atlantic',
 'NY':'Northeast','CT':'Northeast','RI':'Northeast','MA':'Northeast','VT':'Northeast','NH':'Northeast','ME':'Northeast',
}
E = []
def add(name, typ, city, state, org, website, notes=''):
    E.append({'Name': name, 'Type': typ, 'City': city, 'State': state,
              'Region': REGION.get(state, 'National'), 'Organization': org,
              'Website': website, 'Notes': notes})

USYF = 'https://www.usyouthfutsal.com'
# ---------- Organizations ----------
add('US Youth Futsal (USYF)', 'Organization', 'Overland Park', 'KS', 'USYF', USYF, 'Largest US Soccer-affiliated futsal organization — 100+ leagues in 30 states.')
add('U.S. Futsal (USFF)', 'Organization', 'Berkeley', 'CA', 'USFF', 'https://futsal.com', 'United States Futsal Federation — national & regional championships since 1981.')
add('United Futsal', 'Organization', 'Orlando', 'FL', 'United Futsal', 'https://www.unitedfutsal.com', 'Premier youth futsal event organization — World Futsal Championships & Champions Cup Series.')
add('National Futsal Premier League (NFPL)', 'League', 'Chicago', 'IL', 'NFPL', 'https://www.nationalfutsalpremierleague.com', 'Top semi-pro US futsal league (est. 2018) — Men’s & Women’s divisions, USASA-sanctioned.')
add('USYF Academy League', 'League', 'National', 'National', 'USYF', USYF + '/academy', 'Highest level of US youth club futsal competition; qualifies for National Academy Cup.')

# ---------- National tournaments ----------
add('USYF National Championships', 'Tournament', 'Richmond', 'VA', 'USYF', USYF + '/nationals', 'Jul 3-6, 2026 — U9-U19 boys & girls; qualification via 13 regionals.')
add('U.S. Futsal National Championships', 'Tournament', 'National', 'National', 'USFF', 'https://futsalnationalchampionship.com', 'USFF flagship national championship.')
add('World Futsal Championships', 'Tournament', 'Orlando', 'FL', 'United Futsal', 'https://www.unitedfutsal.com/event/world-futsal-championships', 'Jul 14-16, 2026, Orange County Convention Center — largest international youth futsal event in the US.')
add('Champions Cup Series Finals', 'Tournament', 'Orlando', 'FL', 'United Futsal', 'https://www.unitedfutsal.com/champions-cup-series-season-5', 'Jul 17-19, 2026 — season-long Champions Cup Series finals.')
add('World Futsal Cup', 'Tournament', 'National', 'National', 'United Futsal', 'https://www.unitedfutsal.com/world-futsal-cup', 'United Futsal international club event.')
add('USYF National Academy Cup', 'Tournament', 'National', 'National', 'USYF', USYF + '/academy', 'Championship for USYF Academy League clubs.')

# ---------- USYF Regional Championships (13 + Midwest TBD) ----------
regs = [
 ('USYF Southwest Regional Championships','San Diego','CA','Dec 11-13, 2026'),
 ('USYF Northern California Regional Championships','Sacramento','CA','Dec 11-13, 2026'),
 ('USYF South Regional Championships','Houston','TX','Dec 18-20, 2026'),
 ('USYF Atlantic Regional Championships','Manheim','PA','Jan 8-10, 2027'),
 ('USYF Southeast Regional Championships','Fort Myers','FL','Jan 9-10, 2027'),
 ('USYF Great Lakes Regional Championships','Akron','OH','Jan 15-18, 2027'),
 ('USYF South Atlantic Regional Championships','Charlotte','NC','Jan 15-18, 2027'),
 ('USYF Northeast Regional Championships','Boston','MA','Jan 15-18, 2027'),
 ('USYF Mid-Atlantic Regional Championships','Richmond','VA','Jan 22-24, 2027'),
 ('USYF North Regional Championships','Minneapolis','MN','Jan 22-24, 2027'),
 ('USYF Lake Shore Regional Championships','Grand Rapids','MI','Feb 5-7, 2027'),
 ('USYF Central Regional Championships','Overland Park','KS','Feb 12-14, 2027'),
 ('USYF Mid-South Regional Championships','Nashville','TN','Dates TBA'),
 ('USYF Midwest Regional Championships','St. Louis','MO','Location/dates TBD'),
]
for n, c, s, d in regs:
    add(n, 'Tournament', c, s, 'USYF', USYF + '/regional-championships', d + ' — qualifier for USYF Nationals.')

# ---------- USFF regionals ----------
add('U.S. Futsal Northeast Regional Championship', 'Tournament', 'Atlantic City', 'NJ', 'USFF', 'https://northeastfutsalchampionship.com', 'Feb 13-16, 2026, Atlantic City Convention Center.')
add('U.S. Futsal Northwest Regional Championship', 'Tournament', 'San Francisco', 'CA', 'USFF', 'https://northwestfutsalchampionship.com', 'Feb 27 - Mar 1, 2026, Moscone Center.')
add('United Futsal Regional Championship — Cincinnati', 'Tournament', 'Cincinnati', 'OH', 'United Futsal', 'https://www.unitedfutsal.com/event/regional-championship-cincinnati', 'Champions Cup Series regional.')

# ---------- USYF league affiliates (from official league directory) ----------
L = [
 ('Birmingham Futsal','Bessemer','AL'),('FutsalALA','Cullman','AL'),('Omni Futsal','Cullman','AL'),
 ('Arizona Athletic Grounds League','Mesa','AZ'),
 ('530 Futsal','Chico','CA'),('559 Futsal League','Visalia','CA'),('619 Futsal','San Diego','CA'),
 ('Futsal Factory','Sacramento','CA'),('Los Angeles Futsal League','Los Angeles','CA'),('Tri-Valley Futsal League','Pleasanton','CA'),
 ('Futsal Colorado','Denver','CO'),
 ('Florida Futsal Summer League','Deerfield Beach','FL'),('Naples Futsal','Naples','FL'),('Okeechobee United','Okeechobee','FL'),
 ('Orlando Futsal League','Orlando','FL'),('South Florida Super League','Miami','FL'),
 ('GSA Futsal League','Snellville','GA'),('Jaxco Futsal','Hoschton','GA'),('W9 Futsal League','Atlanta','GA'),
 ('Idaho Futsal','Boise','ID'),
 ('G3X Futsal','Elgin','IL'),("Gio's Futsal League",'Chicago','IL'),('Klicsports Futsal League','Naperville','IL'),
 ('Fort Wayne Futsal','Fort Wayne','IN'),('Futsal Indy','Carmel','IN'),('NWI Futsal League','Hammond','IN'),
 ('Des Moines Futsal','Des Moines','IA'),
 ('Heartland Futsal','Overland Park','KS'),('WSF Futsal League','Wichita','KS'),
 ('Louisville Futsal','Louisville','KY'),
 ('Eastern Shore Premier Futsal League','Salisbury','MD'),
 ('Massachusetts Futsal Association','Marlborough','MA'),('Western Massachusetts Futsal','Chicopee','MA'),
 ('East Michigan Futsal','Southfield','MI'),('Ginga Futsal Society League','Grand Rapids','MI'),
 ('Kalamazoo Portage Futsal','Paw Paw','MI'),('Mid Michigan Futsal','Southfield','MI'),('West Michigan Futsal','Grand Rapids','MI'),
 ('Minnesota Futsal','Minneapolis','MN'),
 ('Northland Futsal League','Kansas City','MO'),
 ('Sarpy County Futsal League','Papillion','NE'),
 ('South Jersey Futsal','Sewell','NJ'),
 ('Futsal Rochester','Rochester','NY'),('CNY Futsal','Syracuse','NY'),('Gaffer City FC Futsal','Corning','NY'),
 ('Capital Futsal League','Raleigh','NC'),('F5 Futsal','Charlotte','NC'),('Wilmington NC Futsal','Wilmington','NC'),
 ('937 Futsal League','Dayton','OH'),('Greater Columbus Futsal League (GCFL)','Columbus','OH'),('Great Lakes Futsal','Akron','OH'),
 ('Bucks Futsal','Southampton','PA'),('Philadelphia Futsal League','Philadelphia','PA'),('Pittsburgh Futsal League','Pittsburgh','PA'),
 ('Elite Futsal Charleston','Charleston','SC'),('Grand Strand Futsal Association','Myrtle Beach','SC'),('Soda City Futsal','Irmo','SC'),
 ('Memphis Futsal League','Memphis','TN'),
 ('Austin Youth Futsal League','Austin','TX'),
 ('Central Virginia Futsal','Fredericksburg','VA'),('Futsal RVA','Richmond','VA'),
 ('Hampton Roads Futsal League','Newport News','VA'),('Metro Futsal','Springfield','VA'),
 ('Futsal West Virginia','Morgantown','WV'),
]
for n, c, s in L:
    add(n, 'League', c, s, 'USYF', USYF + '/league-directory', 'USYF league affiliate.')

# ---------- NFPL clubs (2025-26) ----------
NF = 'https://www.nationalfutsalpremierleague.com'
nfpl = [
 ('Anthem Futsal','Rancho Cordova','CA','California Division (M+W) — Omni Arena'),
 ('Bay Area Footy PD','Redwood City','CA','California Division (M+W)'),
 ('HBK Futsal','San Jose','CA','California Division (M+W)'),
 ('Three Sixty Sala','Antioch','CA','California Division (M+W)'),
 ('Brusa FC','Phoenix','AZ','Southwest Division — NFPL champions 2024-25 & 2025-26'),
 ('Los Yunaites','Albuquerque','NM','Southwest Division'),
 ('NM Flagship Futsal','Rio Rancho','NM','Southwest Division — 2025-26 runner-up'),
 ('Santa Fe Gloom','Santa Fe','NM','Southwest Division'),
 ('Capital Futsal','Washington','DC','Midwest Division'),
 ('Futsal Factory Academy','Dexter','MI','Midwest Division — 2024-25 runner-up'),
 ('Inter Detroit','Detroit','MI','Midwest Division'),
 ('MitWest Futsal Club','Chicago','IL','Midwest Division'),
]
for n, c, s, note in nfpl:
    add(n, 'Club / Team', c, s, 'NFPL', NF, note)
# Notable NFPL alumni clubs
add('Grand Rapids OLé', 'Club / Team', 'Grand Rapids', 'MI', 'NFPL', NF, 'NFPL champions 2021-22 & 2023-24.')
add('Columbus Futsal', 'Club / Team', 'Columbus', 'OH', 'NFPL', NF, 'NFPL 2021-22 runner-up; women’s division founding club.')
add('FC Tryzub', 'Club / Team', 'Philadelphia', 'PA', 'NFPL', NF, 'NFPL champions 2022-23.')
add('Colorado Futsal Academy', 'Club / Team', 'Denver', 'CO', 'NFPL', NF, 'NFPL 2023-24 runner-up.')
add('Ann Arbor Mudpuppies', 'Club / Team', 'Ann Arbor', 'MI', 'NFPL', NF, 'NFPL 2018 runner-up.')

# ---------- North Texas / DFW ----------
add('Joga Labs FC', 'Club / Team', 'Keller', 'TX', 'Independent', 'https://jogalab.com', 'Competitive youth futsal club — U9-U15 select teams (Black & Red squads), Chaos Indoor Futsal League. Also soccer classes ages 5-15 and Inspire Labs autism soccer.')
add('Chaos Indoor Futsal League', 'League', 'Keller', 'TX', 'Independent', 'https://scheduler.leaguelobster.com/o/363659/chaos-sports-performance-futsal/', 'Year-round youth futsal league at Chaos Sports Performance, 5701 Egg Farm Rd, Fort Worth, TX 76244.')

json.dump(E, io.open('usa_futsal_directory.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
from collections import Counter
print(len(E), 'entries |', dict(Counter(e['Type'] for e in E)), '|', len(set(e['State'] for e in E)), 'states')

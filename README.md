# README
## Status
*Work in progress*

## Introduction
1. These data are made available by the City of Philadelphia's Mayor's Office of Transportation and Utilities
2. They are available at https://www.opendataphilly.org/dataset/vehicular-crash-data
3. Due to irregularities in accessing the data from the web, I have included the data as part of the repository in the `data` folder.
4. These data contain crash data for the years 2011 through 2014, provided by Pennsylvania Department of Transportation

## Codebook
The following codebook is adapted from the [City of Philadelphia's Mayor's Office of Transportation and Utilities](http://metadata.phila.gov/#home/datasetdetails/5543865420583086178c4eba/).

|Field|Description|Type|
|-----|-----------|----|
|ACCESS_CTRL|Access control code; 1=Limited, 2=Partial, 3=None|str|
|AGE|Age of person|num|
|AUTOMOBILE_COUNT|Nbr of autos involved|num|
|BELTED_DEATH_COUNT|Nbr belted ppl killed|num|
|BELTED_MAJ_INJ_COUNT|Nbr belted ppl w/major injuries|num|
|BICYCLE_COUNT|Nbr bikes involved|num|
|BICYCLE_DEATH_COUNT|Nbr bicyclists killed|num|
|BICYCLE_MAJ_INJ_COUNT|Nbr bicyclists w/major injuries|num|
|BODY_TYPE|Vehicle body type; 1=Convertible, 2=2-door sedan, 3=3-door hatchback, 4=4-door sedan, 5=5-door sedan, 6=station wagon, 8=Other auto, 9=Unk auto, 10=Auto-based pickup, 11=Auto-based panel truck, 12=Compact utility, 13=Large limo, 14=3-wheel auto (or derivative), 15=Large utility, 16=Utility station wagon, 19=Unk utility, 20=Motorcycle, 21=Moped, 22=3-wheeled motorcycle/moped, 23=Off-road motorcycle, 24=ATV, 25=Mini-bike/scooter, 28=Other motorcycle, 29=Unk motorcycle, 30=School bus, 31=Inner-city bus, 32=Transit bus, 38=Other bus, 39=Unk bus, 40=Minivan, 41=Large van, 42=Step-in van, 43=Van-based motor home, 44=Van-based transit bus, 48=Other van, 49=Unk van, 50=Compact pickup, 51=Std pickup, 52=Pickup w/camper, 53=Convertible pickup, 58=Other pickup, 59=Unk pickup, 60=Cab chassis-based, 61=Truck-based panel, 62=Light truck-based motor home, 68=Oth light conventional truck, 69=Unk light truck, 70=Truck (10k-19.5k lbs.), 71=Truck (19.5k-26k lbs.), 72=Truck(26k+ lbs.), 73=Truck (lbs. unk), 74=Medium/heavy motor home, 75=Truck tractor, 76=Big step van, 78=Camper, 79=Unk heavy truck, 80=Snowmobile, 81=Farm equip., 82=Construction equip., 88=Oth special vehicle|num|
|BUS_COUNT|Nbr buses involved|num|
|COLLISION_TYPE|0=Non-collision, 1=Rear-end, 2=Head-on, 3=Rear-to-rear, 4=Angle, 5=Sideswipe (same dir.), 6=Sideswipe (opp. dir.), 7=Fixed object, 8=Hit pedestrian, 9=Oth/unk|num|
|COMM_VEH_COUNT|Nbr comm vehicles involved|num|
|Count_|Nbr crashes in TAZ, 2011-2013|num|
|CRASH_MONTH|Month of crash|num|
|CRASH_YEAR|Year of crash|num|
|CRN|Crash Record Number - PA DOT unique id|num|
|DAY_OF_WEEK|1=Sunday, 2=Monday, 3=Tuesday, 4=Wednesday, 5=Thursday, 6=Friday, 7=Saturday|num|
|FATAL_COUNT|Nbr of fatalities|num|
|HEAVY_TRUCK_COUNT|Nbr heavy trucks involved|num|
|HOUR_OF_DAY|Hour of crash|num|
|Households|Nbr of households in TAZ in 2010|num|
|ILLUMINATION|Lighting at scene; 1=Daylight, 2=Dark, no street lights, 3=Dark, street lights, 4=Dusk, 5=Dawn, 6=Dark, unk lighting, 8=Oth, 9=Unk|num|
|INJURY_COUNT|Nbr ppl sustaining injuries|num|
|INTERSECT_TYPE|Intersection type; 0=Mid-block, 1=4-way, 2='T' intersection, 3='Y' intersection, 4=Traffic circle, 5=Multi-leg intersection, 6=On ramp, 7=Off ramp, 8=Crossover, 9=RR crossing, 10=Oth, 99=Unk|num|
|INTERSECTION|Intersection indicator|bin|
|LANE_COUNT|Nbr of lanes|num|
|LOCATION_TYPE|Crash location; 0=NA, 1=Underpass, 2=Ramp, 3=Bridge, 4=Tunnel, 5=Toll booth, 6=Crossover related, 7=Driveway/parking lot, 8=Ramp and bridge, 9=Unk|num|
|MAJ_INJ_COUNT|Nbr of ppl with major injuries|num|
|MAX_SEVERITY_LEVEL|Maximum severity of injuries; 0=Not injured, 1=Killed, 2=Major injury, 3=Moderate injury, 4=Minor injury, 8=Injury/unk severity, 9=Unk|num|
|MCYCLE_DEATH_COUNT|Nbr motocyclists killed|num|
|MCYCLE_MAJ_INJ_COUNT|Nbr motorcyclists w/major injuries|num|
|MIN_INJ_COUNT|Nbr ppl w/minimal injuries|num|
|MOD_INJ_COUNT|Nbr ppl w/moderate injuries|num|
|MOTORCYCLE_COUNT|Nbr motorcycles involved|num|
|PED_COUNT|Nbr pedestrians involved|num|
|PED_DEATH_COUNT|Nbr pedestrians killed|num|
|PED_MAJ_INJ_COUNT|Nbr pedestrians w/major injuries|num|
|PERSON_COUNT|Nbr total ppl involved|num|
|PERSON_NUM|Crash person number|num|
|PERSON_TYPE|1=Driver, 2=Passenger, 7=Pedestrian, 8=Oth, 9=Unk|num|
|Population|Total population in TAZ for 2010|num|
|RDWY_ORIENT|Roadway orientation; E=East, N=North, S=South, U=Unk, W=West|str|
|RELATION_TO_ROAD|Crash's relativity to road; 1=On roadway, 2=Shoulder, 3=Median, 4=Roadside, 5=Outside trafficway, 6=In parking lane, 7=Gore (intersection of ramp/highway), 9=Unk|num|
|RESTRAINT_HELMET|Restraint or helmet; 0=None or NA, 1=Shoulder belt, 2=Lap belt, 3=Lap and shoulder belts, 4=Child safety seat, 5=Motorcycle helmet, 6=Bicycle helmet, 10=Safety belt (improper), 11=Child safety seat (improper), 12=Helmet (improper), 90=Unk restraint used, 99=Unk|num|
|ROAD_CONDITION|Roadway surface; 0=Dry, 1=Wet, 2=Sand/mud/dirt/oil/gravel, 3=Snow, 4=Slush, 5=Ice, 6=Ice patches, 7=Water (standing/moving), 8=Oth, 9=Unk|num|
|SCH_BUS_IND|School bus involved; 0=No, 1=Yes, 2=Unk|num|
|SCH_ZONE_IND|Occur in school zone; 0=No, 1=Yes, 2=Unk|num|
|female|Sex of individual involved; 0=Male, 1=Female, 2=Unk|num|
|SMALL_TRUCK_COUNT|Nbr small trucks involved|num|
|SPEED_LIMIT|Speed limit at crash|num|
|Sum_BICY_1|Nbr bicyclists killed in crashes in TAZ, 2011-2013|num|
|Sum_BICY_2|Nbr bicyclists w/major injury in crashes in TAZ, 2011-2013|num|
|Sum_FATAL_|Nbr ppl killed in crashes in TAZ, 2011-2013|num|
|Sum_MAJ_IN|Nbr ppl w/major injury in crashes in TAZ, 2011-2013|num|
|Sum_PED_CO|Nbr pedestrians involved in crashes in TAZ, 2011-2013|num|
|Sum_PED_DE|Nbr pedestrians killed in crashes in TAZ, 2011-2013|num|
|Sum_PED_MA|Nbr pedestrians w/major injury in crashes in TAZ, 2011-2013|num|
|Sum_PERSON|Nbr ppl in crashes in TAZ, 2011-2013|num|
|Sum_VEHICL|Nbr vehicles in crashes in TAZ, 2011-2013|num|
|SUV_COUNT|Nbr SUV's in crashes|num|
|TCD_TYPE|Traffic control device; 0=NA, 1=Flashing traffic signal, 2=Traffic signal, 3=Stop sign, 4=Yield sign, 5=Active RR crossing, 6=Passive RR crossing, 7=Police officer, 8=Oth, 9=Unk|num|
|TIME_OF_DAY|Time of day of crash|str|
|Total_Empl|Nbr of jobs in TAZ|num|
|TRANSPORTED|Transport to medical facility; 1=Yes, 0=No|bin|
|TRAVEL_SPD|Travel speed|num|
|UNB_DEATH_COUNT|Nbr ppl killed w/o seatbelt|num|
|UNB_MAJ_INJ_COUNT|Nbr ppl w/major injury w/o seatbelt|num|
|UNBELTED_OCC_COUNT|Nbr unbelted occupants|num|
|UNIT_NUM|Vehicle unit number|num|
|UNK_INJ_DEG_COUNT|Nbr ppl w/injury of unk severity|num|
|UNK_INJ_PER_COUNT|Nbr ppl unk if injured or not|num|
|VAN_COUNT|Nbr vans involved|num|
|VEH_MOVEMENT|1=Going straight, 2=Slowing/stopping in lane, 3=Stopped in lane, 4=Passing vehicle, 5=Leaving parked position, 6=Parked, 7=Entering park position, 8=Trying to avoid something, 9=Right on red, 10=Turning right, 11=Left on red, 12=Turning left, 13=Making U-turn, 14=Backing up, 15=Changing lanes/merging, 16=Negotiating curve right, 17=Negotiating curve left, 98=Oth, 99=Unk|num|
|VEH_TYPE|1=Auto, 2=Motorcycle, 3=Bus, 4=Small truck, 5=Large truck, 6=SUV, 7=Van, 10=Snowmobile, 11=Farm equip, 12=Construction equip, 13=ATV, 18=Oth special vehicle, 20=Uni/bi/tricycle, 21=Oth pedalcycle, 22=Horse/buggy, 23=Horse/rider, 24=Train|num
|VEHICLE_COUNT|Nbr vehicles involved|num|
|VEHICLE_FAILURE|Vehicle failed; 0=No, 1=Yes|bin|
|WEATHER|Weather at crash time; 1=No adverse conditions, 2=Rain, 3=Sleet/hail, 4=Snow, 5=Fog, 6=Rain and fog, 7=Sleet and fog, 8=Oth, 9=Unk|num|

The codebook above *reflects variables after cleaning*. Run the `prep.py` script to clean the original data before conducting analyses. 

## Contact
If there are questions, contact matthew.a.hoover at gmail.com. 
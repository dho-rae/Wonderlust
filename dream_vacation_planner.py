a = "Luxury Escape"
b = "Wellness"
c = "Urban Nightscape"
d = "Gastronomy"
e = "Cultural Immersion"
f = "Adventure Tourism"
g = "Nature Retreat"


class DreamVacationPlanner:
    def __init__(self):
        self.vacation_type_map = {'a': "Luxury Escape", 'b': "Wellness", 'c': "Urban Nightscape", 'd': "Gastronomy",
                                  'e': "Cultural Immersion", 'f': "Adventure Tourism", 'g': "Nature Retreat"}
        self.vacation_type = {"Algarve": {1: a, 2: b}, "Amsterdam": {1: c, 2: e}, "Aspen": {1: f, 2: a},
                              "Bali": {1: b, 2: g}, "Banff": {1: g, 2: f}, "Bangkok": {1: c, 2: d},
                              "Barcelona": {1: d, 2: c}, "Bergen": {1: g, 2: b}, "Berlin": {1: e, 2: c},
                              "Bora Bora": {1: a, 2: f}, "Borneo": {1: g, 2: f}, "Bruges": {1: e, 2: d},
                              "Budapest": {1: e, 2: c}, "Buenos Aires": {1: c, 2: e}, "Budva": {1: a, 2: f},
                              "Byron Bay": {1: g, 2: b}, "Cape Town": {1: f, 2: d}, "Cancun": {1: a, 2: f},
                              "Capri": {1: a, 2: d}, "Chiang Mai": {1: b, 2: g}, "Cusco": {1: f, 2: g},
                              "Da Nang": {1: g, 2: b}, "Dolomites": {1: f, 2: g}, "Dubai": {1: c, 2: a},
                              "Dublin": {1: e, 2: c}, "Dubrovnik": {1: e, 2: g}, "Edinburgh": {1: e, 2: c},
                              "Gran Canaria": {1: g, 2: b}, "Granada": {1: e, 2: g}, "Goa": {1: b, 2: d},
                              "Hanoi": {1: d, 2: e}, "Ho Chi Minh": {1: e, 2: d}, "Hoi An": {1: b, 2: d},
                              "Honolulu": {1: a, 2: b}, "Hong Kong": {1: d, 2: c}, "Ibiza": {1: c, 2: d},
                              "Istanbul": {1: d, 2: b}, "Koh Samui": {1: b, 2: a}, "Kyoto": {1: e, 2: g},
                              "Lake Como": {1: a, 2: g}, "Las Vegas": {1: c, 2: a}, "Lisbon": {1: d, 2: e},
                              "Livigno": {1: f, 2: g}, "London": {1: e, 2: c}, "Manila": {1: d, 2: c},
                              "Marrakech": {1: d, 2: a}, "Medellín": {1: c, 2: e}, "Mexico City": {1: c, 2: d},
                              "Miami": {1: c, 2: a}, "Monte Carlo": {1: a, 2: c}, "Naples": {1: d, 2: e},
                              "Napa Valley": {1: a, 2: d}, "New Orleans": {1: c, 2: d}, "New York City": {1: e, 2: c},
                              "Palawan": {1: g, 2: b}, "Palm Springs": {1: a, 2: b}, "Paris": {1: d, 2: a},
                              "Patagonia": {1: g, 2: f}, "Phuket": {1: a, 2: f}, "Porto": {1: e, 2: d},
                              "Pokhara": {1: f, 2: g}, "Queenstown": {1: f, 2: a}, "Reykjavik": {1: f, 2: c},
                              "Rishikesh": {1: b, 2: f}, "Rio ee Janeiro": {1: c, 2: f}, "Rome": {1: e, 2: d},
                              "Rotorua": {1: f, 2: g}, "Saint-Tropez": {1: a, 2: c}, "Salzburg": {1: g, 2: e},
                              "Santa Barbara": {1: a, 2: b}, "Santa Fe": {1: b, 2: e}, "Santorini": {1: a, 2: b},
                              "São Paulo": {1: c, 2: d}, "Sedona": {1: b, 2: f}, "Seville": {1: e, 2: d},
                              "Shanghai": {1: c, 2: e}, "Siem Reap": {1: e, 2: f}, "Singapore": {1: d, 2: c},
                              "Taghazout": {1: f, 2: b}, "Taipei": {1: d, 2: c}, "Tamarindo": {1: b, 2: f},
                              "Tokyo": {1: c, 2: e}, "Tuscany": {1: a, 2: g}, "Tulum": {1: b, 2: g},
                              "Valencia": {1: d, 2: e}, "Vancouver": {1: g, 2: f}, "Venice": {1: e, 2: a},
                              "Whistler": {1: f, 2: g}, "Zermatt": {1: f, 2: a}}
        self.cheapest_flight = {"BOS": {"Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica",
                                        "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala",
                                        "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama",
                                        "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
                                        "Suriname", "Trinidad and Tobago", "United States"},
                                "IST": {"Afghanistan", "Albania", "Algeria", "Angola", "Argentina", "Armenia",
                                        "Azerbaijan", "Bahrain", "Belarus", "Benin", "Bosnia and Herzegovina",
                                        "Botswana", "Brazil", "Bulgaria", "Burkina Faso", "Burundi", "Cape Verde",
                                        "Central African Republic", "Chad", "Chile", "Colombia", "Comoros", "Congo",
                                        "Croatia", "Cyprus", "Democratic Republic of the Congo", "Djibouti", "Egypt",
                                        "Equatorial Guinea", "Eritrea", "Estonia", "Swaziland", "Ethiopia", "Gabon",
                                        "Gambia", "Georgia", "Ghana", "Greece", "Guinea", "Guinea-Bissau", "Hungary",
                                        "Iran", "Iraq", "Israel", "Ivory Coast", "Jordan", "Kazakhstan", "Kenya",
                                        "Kuwait", "Kyrgyzstan", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
                                        "Lithuania", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius",
                                        "Moldova", "Montenegro", "Mozambique", "Namibia", "Niger", "Nigeria",
                                        "North Macedonia", "Oman", "Pakistan", "Palestine", "Poland", "Qatar",
                                        "Romania", "Russia", "Rwanda", "Sao Tome and Principe", "Saudi Arabia",
                                        "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Slovakia", "Slovenia",
                                        "Somalia", "South Africa", "South Korea", "South Sudan", "Sri Lanka", "Sudan",
                                        "Syria", "Taiwan", "Tajikistan", "Tanzania", "Togo", "Tunisia", "Turkey",
                                        "Turkmenistan", "Uganda", "Ukraine", "United Arab Emirates", "Uzbekistan",
                                        "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"},
                                "SIN": {"Australia", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Fiji",
                                        "India", "Indonesia", "Japan", "Kiribati", "Laos", "Malaysia", "Maldives",
                                        "Marshall Islands", "Micronesia", "Myanmar", "Nauru", "Nepal",
                                        "New Zealand", "North Korea", "Palau", "Papua New Guinea", "Philippines",
                                        "Samoa", "Singapore", "Solomon Islands", "Sri Lanka", "Thailand", "Timor-Leste",
                                        "Tonga", "Tuvalu", "Vanuatu", "Vietnam"},
                                "LHR": {"Andorra", "Austria", "Belgium", "Czech Republic", "Denmark", "France",
                                        "Finland", "Germany", "Iceland", "Ireland", "Italy", "Liechtenstein",
                                        "Luxembourg", "Malta", "Monaco", "Morocco", "Netherlands", "Norway", "Portugal",
                                        "San Marino", "Spain", "Sweden", "Switzerland", "United Kingdom",
                                        "Vatican City"}}
        self.closeness = {"BOS": {"Aspen": 1, "Banff": 1, "Buenos Aires": 2, "Cancun": 1, "Cusco": 1, "Honolulu": 1,
                                  "Istanbul": 2, "Las Vegas": 1, "London": 2, "Medellín": 1, "Mexico City": 1,
                                  "Miami": 1, "Napa Valley": 1, "New Orleans": 1, "New York City": 1, "Palm Springs": 1,
                                  "Patagonia": 1, "Reykjavik": 2, "Rio de Janeiro": 1, "Santa Barbara": 1,
                                  "Santa Fe": 1, "São Paulo": 2, "Sedona": 1, "Taghazout": 1, "Tamarindo": 1,
                                  "Tulum": 1, "Vancouver": 1, "Whistler": 1},
                          "LHR": {"Algarve": 1, "Amsterdam": 1, "Aspen": 2, "Banff": 2, "Bangkok": 2, "Barcelona": 1,
                                  "Bergen": 1, "Berlin": 1, "Borneo": 2, "Bruges": 1, "Budapest": 2, "Budva": 1,
                                  "Byron Bay": 2, "Cape Town": 1, "Cancun": 2, "Capri": 1, "Chiang Mai": 2,
                                  "Da Nang": 2, "Dolomites": 1, "Dubai": 2, "Dublin": 1, "Dubrovnik": 2, "Edinburgh": 1,
                                  "Gran Canaria": 2, "Granada": 1, "Goa": 2, "Hanoi": 2, "Ho Chi Minh": 2, "Hoi An": 2,
                                  "Hong Kong": 2, "Ibiza": 1, "Istanbul": 1, "Koh Samui": 2, "Kyoto": 2, "Lake Como": 1,
                                  "Las Vegas": 2, "Lisbon": 1, "Livigno": 1, "Manila": 1, "Marrakech": 2, "Medellín": 2,
                                  "Mexico City": 2, "Miami": 2, "Monte Carlo": 1, "Naples": 1, "Napa Valley": 2,
                                  "New Orleans": 2, "New York City": 2, "Palawan": 2, "Palm Springs": 2, "Paris": 1,
                                  "Phuket": 2, "Porto": 1, "Queenstown": 2, "Reykjavik": 1, "Rishikesh": 2, "Rome": 1,
                                  "Rotorua": 2, "Saint-Tropez": 1, "Salzburg": 2, "Santa Barbara": 1, "Santa Fe": 1,
                                  "Santorini": 2, "Sedona": 1, "Seville": 1, "Shanghai": 2, "Siem Reap": 2,
                                  "Singapore": 2, "Taghazout": 1, "Taipei": 1, "Tamarindo": 2, "Tokyo": 2, "Tuscany": 1,
                                  "Tulum": 1, "Valencia": 1, "Vancouver": 2, "Venice": 1, "Whistler": 1, "Zermatt": 2},
                          "IST": {"Algarve": 2, "Amsterdam": 2, "Bali": 1, "Banff": 2, "Bangkok": 1, "Barcelona": 2,
                                  "Bergen": 2, "Berlin": 2, "Bora Bora": 1, "Borneo": 1, "Bruges": 2, "Budapest": 1,
                                  "Budva": 2, "Byron Bay": 1, "Cape Town": 2, "Capri": 2, "Chiang Mai": 1, "Cusco": 2,
                                  "Da Nang": 1, "Dolomites": 2, "Dubai": 1, "Dublin": 2, "Dubrovnik": 1, "Edinburgh": 2,
                                  "Gran Canaria": 1, "Granada": 2, "Goa": 1, "Hanoi": 1, "Ho Chi Minh": 1, "Hoi An": 1,
                                  "Hong Kong": 1, "Ibiza": 2, "Koh Samui": 1, "Kyoto": 1, "Lake Como": 2, "Lisbon": 2,
                                  "Livigno": 2, "London": 1, "Manila": 4, "Marrakech": 2, "Medellín": 1,
                                  "Mexico City": 1, "Miami": 1, "Monte Carlo": 2, "Naples": 2, "Napa Valley": 2,
                                  "New Orleans": 1, "New York City": 1, "Palm Springs": 1, "Paris": 2, "Patagonia": 2,
                                  "Phuket": 1, "Porto": 2, "Pokhara": 2, "Queenstown": 1, "Reykjavik": 1,
                                  "Rishikesh": 2, "Rio de Janeiro": 2, "Rome": 2, "Rotorua": 1, "Saint-Tropez": 2,
                                  "Salzburg": 1, "Santa Barbara": 2, "Santa Fe": 2, "Santorini": 1, "São Paulo": 1,
                                  "Sedona": 2, "Seville": 2, "Shanghai": 1, "Siem Reap": 1, "Singapore": 2,
                                  "Taghazout": 2, "Taipei": 2, "Tamarindo": 1, "Tokyo": 1, "Tuscany": 2, "Tulum": 2,
                                  "Valencia": 2, "Vancouver": 1, "Venice": 2, "Whistler": 2, "Zermatt": 1},
                          "SIN": {"Aspen": 2, "Bali": 1, "Bangkok": 1, "Bora Bora": 2, "Borneo": 1, "Budapest": 1,
                                  "Byron Bay": 1, "Chiang Mai": 1, "Da Nang": 1, "Dubai": 1, "Dubrovnik": 1,
                                  "Gran Canaria": 2, "Goa": 1, "Hanoi": 1, "Ho Chi Minh": 1, "Hoi An": 1, "Honolulu": 2,
                                  "Hong Kong": 1, "Istanbul": 2, "Koh Samui": 1, "Kyoto": 1, "London": 2, "Palawan": 1,
                                  "Patagonia": 2, "Phuket": 1, "Queenstown": 2, "Rotorua": 2, "Santorini": 2,
                                  "São Paulo": 1, "Shanghai": 1, "Siem Reap": 1, "Tokyo": 1, "Zermatt": 1}}
        self.hot_season = {"January": {"Cape Town", "Hanoi", "Ho Chi Minh", "Koh Samui", "Palawan", "Phuket",
                                       "Rio de Janeiro", "Rotorua", "Siem Reap", "Tamarindo", "Tulum"},
                           "February": {"Ho Chi Minh", "Manila", "Phuket", "Rio de Janeiro", "Tamarindo", "Tokyo"},
                           "March": {"Bangkok", "Da Nang", "Goa", "Hanoi", "Manila", "Mexico City", "Palawan",
                                     "Pokhara", "Siem Reap"},
                           "April": {"Bali", "Borneo", "Hoi An", "Pokhara", "Rishikesh", "Siem Reap", "Tamarindo"},
                           "May": {"Bali", "Borneo", "Cusco", "Da Nang", "Hanoi", "Hoi An", "Palawan", "Rishikesh"},
                           "June": {"Algarve", "Amsterdam", "Aspen", "Banff", "Barcelona", "Bergen", "Berlin", "Bruges",
                                    "Budapest", "Budva", "Byron Bay", "Cape Town", "Dubrovnik", "Edinburgh",
                                    "Gran Canaria", "Granada", "Hoi An", "Honolulu", "Hong Kong", "Ibiza", "Istanbul",
                                    "Koh Samui", "Kyoto", "Lake Como", "Las Vegas", "Lisbon", "Livigno", "London",
                                    "Marrakech", "Medellín", "Miami", "Monte Carlo", "Naples", "Napa Valley",
                                    "New Orleans", "New York City", "Palawan", "Palm Springs", "Paris", "Patagonia",
                                    "Phuket", "Porto", "Queenstown", "Reykjavik", "Rome", "Saint-Tropez", "Salzburg",
                                    "Santa Barbara", "Santa Fe", "Santorini", "Sedona", "Seville", "Shanghai",
                                    "Singapore", "Taghazout", "Taipei", "Tokyo", "Tuscany", "Valencia", "Vancouver",
                                    "Venice", "Whistler", "Zermatt"},
                           "July": {"Algarve", "Amsterdam", "Aspen", "Banff", "Barcelona", "Bergen", "Berlin", "Bruges",
                                    "Budapest", "Budva", "Byron Bay", "Cape Town", "Dubrovnik", "Edinburgh",
                                    "Gran Canaria", "Granada", "Hoi An", "Honolulu", "Hong Kong", "Ibiza", "Istanbul",
                                    "Koh Samui", "Kyoto", "Lake Como", "Las Vegas", "Lisbon", "Livigno", "London",
                                    "Marrakech", "Medellín", "Miami", "Monte Carlo", "Naples", "Napa Valley",
                                    "New Orleans", "New York City", "Palawan", "Palm Springs", "Paris", "Patagonia",
                                    "Phuket", "Porto", "Queenstown", "Reykjavik", "Rome", "Saint-Tropez", "Salzburg",
                                    "Santa Barbara", "Santa Fe", "Santorini", "Sedona", "Seville", "Shanghai",
                                    "Singapore", "Taghazout", "Taipei", "Tokyo", "Tuscany", "Valencia", "Vancouver",
                                    "Venice", "Whistler", "Zermatt"},
                           "August": {"Algarve", "Amsterdam", "Aspen", "Banff", "Barcelona", "Bergen", "Berlin",
                                      "Bruges", "Budapest", "Budva", "Byron Bay", "Cape Town", "Dubrovnik", "Edinburgh",
                                      "Gran Canaria", "Granada", "Hoi An", "Honolulu", "Hong Kong", "Ibiza", "Istanbul",
                                      "Koh Samui", "Kyoto", "Lake Como", "Las Vegas", "Lisbon", "Livigno", "London",
                                      "Marrakech", "Medellín", "Miami", "Monte Carlo", "Naples", "Napa Valley",
                                      "New Orleans", "New York City", "Palawan", "Palm Springs", "Paris", "Patagonia",
                                      "Phuket", "Porto", "Queenstown", "Reykjavik", "Rome", "Saint-Tropez", "Salzburg",
                                      "Santa Barbara", "Santa Fe", "Santorini", "Sedona", "Seville", "Shanghai",
                                      "Singapore", "Taghazout", "Taipei", "Tokyo", "Tuscany", "Valencia", "Vancouver",
                                      "Venice", "Whistler", "Zermatt"},
                           "September": {"Bali", "Bora Bora", "Borneo", "Dubai", "Hong Kong", "Shanghai", "Taipei"},
                           "October": {"Bali", "Bora Bora", "Borneo", "Shanghai", "Taipei"},
                           "November": {"Goa", "Siem Reap"},
                           "December": {"Buenos Aires", "Byron Bay", "Cape Town", "Medellín", "Patagonia", "Queenstown",
                                        "Rio de Janeiro", "Rotorua", "Santa Fe", "São Paulo", "Tamarindo", "Tulum"}}
        self.cold_season = {"January": {"Algarve", "Amsterdam", "Aspen", "Bali", "Banff", "Bangkok", "Barcelona",
                                        "Bergen", "Berlin", "Bruges", "Budapest", "Budva", "Cancun", "Capri",
                                        "Chiang Mai", "Da Nang", "Dolomites", "Dubai", "Dublin", "Dubrovnik",
                                        "Edinburgh", "Gran Canaria", "Granada", "Hanoi", "Ho Chi Minh", "Hoi An",
                                        "Honolulu", "Hong Kong", "Ibiza", "Istanbul", "Kyoto", "Lake Como", "Las Vegas",
                                        "Lisbon", "Livigno", "London", "Manila", "Marrakech", "Miami", "Monte Carlo",
                                        "Naples", "Napa Valley", "New Orleans", "New York City", "Palawan",
                                        "Palm Springs", "Paris", "Phuket", "Porto", "Pokhara", "Reykjavik", "Rishikesh",
                                        "Rome", "Saint-Tropez", "Salzburg", "Santa Barbara", "Santa Fe", "Santorini",
                                        "Sedona", "Seville", "Shanghai", "Singapore", "Taghazout", "Taipei", "Tokyo",
                                        "Tuscany", "Valencia", "Vancouver", "Venice", "Whistler", "Zermatt"},
                            "February": {"Algarve", "Amsterdam", "Aspen", "Bali", "Banff", "Bangkok", "Barcelona",
                                         "Bergen", "Berlin", "Bruges", "Budapest", "Budva", "Cancun", "Capri",
                                         "Chiang Mai", "Cusco", "Da Nang", "Dolomites", "Dubai", "Dublin", "Dubrovnik",
                                         "Edinburgh", "Gran Canaria", "Granada", "Hanoi", "Hoi An", "Honolulu",
                                         "Hong Kong", "Ibiza", "Istanbul", "Kyoto", "Lake Como", "Las Vegas", "Lisbon",
                                         "Livigno", "London", "Manila", "Marrakech", "Miami", "Monte Carlo", "Naples",
                                         "Napa Valley", "New Orleans", "New York City", "Palawan", "Palm Springs",
                                         "Paris", "Phuket", "Porto", "Pokhara", "Reykjavik", "Rome", "Saint-Tropez",
                                         "Salzburg", "Santa Barbara", "Santa Fe", "Santorini", "Sedona", "Seville",
                                         "Shanghai", "Singapore", "Taghazout", "Taipei", "Tokyo", "Tuscany", "Valencia",
                                         "Vancouver", "Venice", "Whistler", "Zermatt"},
                            "March": {"Bali", "Bora Bora", "Cusco"},
                            "April": {"Bora Bora", "Cusco"},
                            "June": {"Buenos Aires", "Byron Bay", "Cape Town", "Goa", "Medellín", "Patagonia",
                                     "Queenstown", "Rio de Janeiro", "Rishikesh", "Saint-Tropez", "São Paulo",
                                     "Tamarindo", "Tulum"},
                            "July": {"Buenos Aires", "Byron Bay", "Cape Town", "Goa", "Medellín", "Patagonia",
                                     "Queenstown", "Rio de Janeiro", "Rishikesh", "Saint-Tropez", "São Paulo",
                                     "Tamarindo", "Tulum"},
                            "August": {"Buenos Aires", "Byron Bay", "Cape Town", "Goa", "Medellín", "Patagonia",
                                       "Queenstown", "Rio de Janeiro", "Rishikesh", "Saint-Tropez", "São Paulo",
                                       "Tamarindo", "Tulum"},
                            "September": {"Goa"},
                            "November": {"Bali", "Bangkok", "Borneo", "Chiang Mai", "Ho Chi Minh", "Mexico City",
                                         "Phuket", "Rishikesh"},
                            "December": {"Algarve", "Amsterdam", "Aspen", "Bali", "Banff", "Bangkok", "Barcelona",
                                         "Bergen", "Berlin", "Bora Bora", "Borneo", "Bruges", "Budapest", "Budva",
                                         "Cancun", "Capri", "Chiang Mai", "Da Nang", "Dolomites", "Dubai", "Dublin",
                                         "Dubrovnik", "Edinburgh", "Gran Canaria", "Granada", "Hanoi", "Honolulu",
                                         "Hong Kong", "Ibiza", "Istanbul", "Koh Samui", "Kyoto", "Lake Como",
                                         "Las Vegas", "Lisbon", "Livigno", "London", "Manila", "Marrakech",
                                         "Mexico City", "Miami", "Monte Carlo", "Naples", "Napa Valley", "New Orleans",
                                         "New York City", "Palawan", "Palm Springs", "Paris", "Phuket", "Porto",
                                         "Pokhara", "Queenstown", "Reykjavik", "Rishikesh", "Rome", "Saint-Tropez",
                                         "Salzburg", "Santa Barbara", "Santa Fe", "Santorini", "Sedona", "Seville",
                                         "Shanghai", "Singapore", "Taghazout", "Taipei", "Tokyo", "Tuscany", "Valencia",
                                         "Vancouver", "Venice", "Whistler", "Zermatt"}}
        self.low_budget_season = {"January": {"Algarve", "Amsterdam", "Bali", "Banff", "Bangkok", "Barcelona", "Bergen",
                                              "Berlin", "Bruges", "Budapest", "Cape Town", "Capri", "Granada", "Hanoi",
                                              "Honolulu", "Ibiza", "Kyoto", "Lake Como", "Las Vegas", "Lisbon",
                                              "Livigno", "London", "Manila", "Mexico City", "Monte Carlo", "Naples",
                                              "Napa Valley", "New York City", "Palawan", "Palm Springs", "Paris",
                                              "Phuket", "Porto", "Reykjavik", "Rome", "Saint-Tropez", "Salzburg",
                                              "Santa Barbara", "Santa Fe", "Santorini", "Seville", "Taghazout",
                                              "Taipei", "Tuscany", "Valencia", "Vancouver", "Venice"},
                                  "February": {"Bali", "Barcelona", "Bergen", "Berlin", "Bora Bora", "Borneo", "Bruges",
                                               "Budapest", "Cancun", "Cape Town", "Capri", "Chiang Mai", "Cusco",
                                               "Da Nang", "Dolomites", "Granada", "Hoi An", "Hanoi", "Honolulu",
                                               "Ibiza", "Kyoto", "Lake Como", "Las Vegas", "Lisbon", "Livigno",
                                               "London", "Manila", "Monte Carlo", "Naples", "Napa Valley",
                                               "New York City", "Palawan", "Palm Springs", "Paris", "Porto",
                                               "Queenstown", "Rome", "Saint-Tropez", "Salzburg", "Santa Barbara",
                                               "Santa Fe", "Santorini", "Seville", "Singapore", "Taipei", "Tuscany",
                                               "Valencia", "Vancouver", "Venice", "Whistler", "Zermatt"},
                                  "March": {"Budva", "Dubrovnik", "Hoi An", "Medellín", "Rishikesh", "Santorini",
                                            "Tokyo"},
                                  "April": {"Aspen", "Bali", "Banff", "Bangkok", "Da Nang", "Dubai", "Dubrovnik",
                                            "Gran Canaria", "Honolulu", "Hong Kong", "Ibiza", "Koh Samui", "Palawan",
                                            "Phuket", "Queensland", "Siem Reap", "Whistler"},
                                  "May": {"Aspen", "Bali", "Bangkok", "Budva", "Byron Bay", "Cape Town", "Da Nang",
                                          "Dubrovnik", "Gran Canaria", "Ho Chi Minh", "Honolulu", "Hong Kong",
                                          "Koh Samui", "Las Vegas", "Medellín", "Mexico City", "New Orleans",
                                          "Patagonia", "Phuket", "Queenstown", "Reykjavik", "Rome", "Rotorua",
                                          "Saint-Tropez", "Santa Barbara", "Santa Fe", "Siem Reap", "São Paulo",
                                          "Sedona", "Tulum", "Valencia", "Vancouver", "Venice", "Whistler", "Zermatt"},
                                  "June": {"Aspen", "Barcelona", "Budva", "Byron Bay", "Cape Town", "Dubai",
                                           "Ho Chi Minh", "Las Vegas", "Manila", "Medellín", "Miami", "New Orleans",
                                           "Palawan", "Palm Springs", "Phuket", "Rio de Janeiro", "São Paulo",
                                           "Siem Reap", "Singapore", "Tamarindo"},
                                  "July": {"Aspen", "Barcelona", "Budva", "Byron Bay", "Cape Town", "Dubai",
                                           "Ho Chi Minh", "Las Vegas", "Manila", "Medellín", "Miami", "New Orleans",
                                           "Palawan", "Palm Springs", "Phuket", "Rio de Janeiro", "São Paulo",
                                           "Siem Reap", "Singapore", "Tamarindo"},
                                  "August": {"Aspen", "Barcelona", "Budva", "Byron Bay", "Cape Town", "Dubai",
                                             "Ho Chi Minh", "Las Vegas", "Manila", "Medellín", "Miami", "New Orleans",
                                             "Palawan", "Palm Springs", "Phuket", "Rio de Janeiro", "São Paulo",
                                             "Siem Reap", "Singapore", "Tamarindo"},
                                  "September": {"Aspen", "Banff", "Bangkok", "Cancun", "Da Nang", "Ho Chi Minh",
                                                "Honolulu", "Hong Kong", "Koh Samui", "Las Vegas", "Medellín", "Miami",
                                                "Monte Carlo", "New Orleans", "Phuket", "Tamarindo"},
                                  "October": {"Aspen", "Banff", "Bangkok", "Bergen", "Budva", "Byron Bay", "Cancun",
                                              "Dubrovnik", "Hanoi", "Ho Chi Minh", "Honolulu", "Hong Kong", "Koh Samui",
                                              "Reykjavik", "Rishikesh", "Siem Reap", "Tamarindo", "Zermatt"},
                                  "November": {"Algarve", "Amsterdam", "Aspen", "Barcelona", "Bergen", "Berlin",
                                               "Bora Bora", "Borneo", "Bruges", "Budapest", "Cape Town", "Capri",
                                               "Dubrovnik", "Gran Canaria", "Honolulu", "Hong Kong", "Istanbul",
                                               "Koh Samui", "Lake Como", "Las Vegas", "Lisbon", "London", "Marrakech",
                                               "Monte Carlo", "Naples", "Napa Valley", "New York City", "Paris",
                                               "Porto", "Rome", "Saint-Tropez", "Salzburg", "Santa Barbara", "Santa Fe",
                                               "Tuscany", "Valencia", "Vancouver", "Venice", "Whistler"},
                                  "December": {"Algarve", "Aspen", "Bali", "Banff", "Barcelona", "Bergen", "Bora Bora",
                                               "Bruges", "Budapest", "Budva", "Cancun", "Capri", "Chiang Mai",
                                               "Da Nang", "Dolomites", "Dubai", "Dublin", "Granada", "Ibiza", "Kyoto",
                                               "Lake Como", "Las Vegas", "Lisbon", "Livigno", "London", "Manila",
                                               "Mexico City", "Monte Carlo", "Naples", "Napa Valley", "New York City",
                                               "Palawan", "Palm Springs", "Paris", "Porto", "Reykjavik", "Rome",
                                               "Sedona", "Seville", "Shanghai", "Taghazout", "Taipei", "Tokyo",
                                               "Valencia", "Vancouver", "Venice", "Whistler", "Zermatt"}}
        # Initialize instance variables
        self.travel_month = None
        self.prime_importance = None
        self.secondary_importance = None
        self.country = None
        self.budget_value = None
        self.airport = None
        self.original_options = set()
        self.options = set()

    def get_travel_month(self):
        while True:
            try:
                answer = input("Are you tied to travelling in a particular month? (Yes / No): ").strip().lower()
                # Input validation
                if answer not in {"yes", "no"}:
                    raise ValueError("Sorry, I didn't quite catch that. Could you try entering either Yes or No?")
                if answer == "yes":
                    while True:
                        month = input("Which month? ").strip().capitalize()
                        if month in {"January", "February", "March", "April", "May", "June",
                                     "July", "August", "September", "October", "November", "December"}:
                            # If a valid month is entered, set the travel_month attribute
                            self.travel_month = month
                            break
                        else:
                            print("Sorry, I didn't quite catch that. Could you check your spelling.")
                else:
                    self.travel_month = None
                break
            except ValueError as ve:
                print(ve)

    def get_prime_importance(self):
        while True:
            try:
                prime_answer = int(input("What is of utmost importance to you? (1. Vacation Type/ 2. Low-Budget/ "
                                         "3. Season): "))
                # Input validation
                if prime_answer not in range(1, 4):
                    raise ValueError("Sorry, I didn't quite catch that. Could you try entering either 1 / 2 / 3? ")
                # Set the prime_importance attribute based on user input
                self.prime_importance = prime_answer
                if prime_answer == 1:
                    # If vacation type is chosen, call choose_vacation_types method
                    self.prime_importance = self.choose_vacation_types()
                elif prime_answer == 2:
                    # If low budget is chosen, call get_country_and_budget method
                    self.prime_importance = self.get_country_and_budget()
                elif prime_answer == 3:
                    # If season is chosen, call choose_season method
                    self.prime_importance = self.choose_season()
                break
            except ValueError:
                print(f"Sorry, I didn't quite catch that. Could you try again? ")

    def choose_vacation_types(self):
        while True:
            try:
                print("Select two vacation types in order of preference:")
                print("a) Luxury Escape, b) Wellness, c) Urban Nightscape, d) Gastronomy, e) Cultural Immersion, "
                      "f) Adventure Tourism, g) Nature Retreat")
                first_choice = input("First choice: ").strip().lower()
                second_choice = input("Second choice: ").strip().lower()
                valid_choices = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
                if first_choice not in valid_choices or second_choice not in valid_choices:
                    raise ValueError("Sorry, I didn't quite catch that. Could you try entering either a / b / c / d / "
                                     "e / f / g? ")
                first_vacation_type = self.vacation_type_map.get(first_choice)
                second_vacation_type = self.vacation_type_map.get(second_choice)
                # Filter vacation types based on user preferences
                options = self.filter_vacation_types(first_vacation_type, second_vacation_type)
                options = set(options.keys())
                print("Interesting...")
                # print("So far I'm thinking...", options)
                return options
            except KeyError:
                print("Sorry, I didn't quite catch that. Could you try entering either a / b / c / d / e / f / g? ")

    def filter_vacation_types(self, first_choice, second_choice):
        options = self.vacation_type.copy()
        for vacation, prefs in self.vacation_type.items():
            if prefs[1] != first_choice or prefs[2] != second_choice:
                del options[vacation]
        return options

    def get_country_and_budget(self):
        while True:
            try:
                departure_city = input("Which country will you be flying from? ").strip()
                airport = None
                for key, value in self.cheapest_flight.items():
                    if departure_city in value:
                        airport = key
                        break
                if not airport:
                    raise ValueError("Sorry, I couldn't find a suitable airport for the country you entered.")
                print(f"I recommend flying from this airport: {airport}")
                cities = self.closeness.get(airport, {})
                options = set(cities.keys())
                while True:
                    budget_input = input("How (in)flexible is your budget? 1) Tight, 2) Moderate: ").strip()
                    if budget_input not in range(1, 3):
                        print("Please enter either 1 or 2.")
                        continue
                    budget_value = int(budget_input)
                    if budget_value == 1:
                        options = {city for city, value in cities.items() if value == 1}
                        # print(f"So far I'm thinking... {options}")
                        break
                    elif budget_value == 2:
                        options = {city for city, value in cities.items() if value in {1, 2}}
                        # print(f"So far I'm thinking... {options}")
                        break
                if self.travel_month:
                    options2 = self.low_budget_season.get(self.travel_month, set())
                    options = options.intersection(options2)
                print("Interesting...")
                # print(f"So far I'm thinking... {options}")
                return options
            except ValueError as ve:
                print(ve)

    def choose_season(self):
        while True:
            try:
                answer = int(input("Which season would you prefer to travel in? (1. Hot/ 2. Cold): "))
                if answer not in range(1, 3):
                    raise ValueError("Sorry, I didn't quite catch that. Could you try entering either Hot / Cold? ")
                if answer == 1:
                    if self.travel_month:
                        options = self.hot_season.get(self.travel_month, set())
                    else:
                        options = set(city for city_set in self.hot_season.values() for city in city_set)
                elif answer == 2:
                    if self.travel_month:
                        options = self.cold_season.get(self.travel_month, set())
                    else:
                        options = set(city for city_set in self.cold_season.values() for city in city_set)
                self.options = options
                print("Interesting...")
                # print(f"So far I'm thinking... {self.options}")
                return options
            except ValueError:
                print(f"Sorry, I didn't quite catch that. Could you try again? ")

    def get_secondary_importance(self):
        secondary_answer = int(
            input("What is of secondary importance to you? (1. Vacation Type/ 2. Low-Budget/ 3. Season): "))
        if secondary_answer not in range(1, 4):
            raise ValueError("Sorry, I didn't quite catch that. Could you try entering either 1 / 2 / 3? ")
        self.secondary_importance = secondary_answer
        if secondary_answer == 1:
            self.secondary_importance = self.choose_secondary_vacation_types()
        elif secondary_answer == 2:
            self.secondary_importance = self.get_secondary_country_and_budget()
        elif secondary_answer == 3:
            self.secondary_importance = self.choose_secondary_season()

    def choose_secondary_vacation_types(self):
        while True:
            try:
                print("Select two vacation types in order of preference:")
                print("a) Luxury Escape, b) Wellness, c) Urban Nightscape, d) Gastronomy, e) Cultural Immersion, "
                      "f) Adventure Tourism, g) Nature Retreat")
                first_choice = input("First choice: ").strip().lower()
                second_choice = input("Second choice: ").strip().lower()
                valid_choices = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
                if first_choice not in valid_choices or second_choice not in valid_choices:
                    raise ValueError("Sorry, I didn't quite catch that. Could you try entering either a / b / c / d / "
                                     "e / f / g? ")
                first_vacation_type = self.vacation_type_map.get(first_choice)
                second_vacation_type = self.vacation_type_map.get(second_choice)
                # Filter vacation types based on user preferences
                options = self.filter_vacation_types(first_vacation_type, second_vacation_type)
                options = set(options.keys())
                print("Interesting...")
                # print("So far I'm thinking...", options)
                return options
            except ValueError:
                continue

    def filter_secondary_vacation_types(self, first_choice, second_choice):
        options = self.vacation_type.copy()
        for vacation, prefs in self.vacation_type.items():
            if prefs[1] != first_choice or prefs[2] != second_choice:
                del options[vacation]
        return options

    def get_secondary_country_and_budget(self):
        while True:
            try:
                departure_city = input("Which country will you be flying from? ").strip()
                airport = None
                for key, value in self.cheapest_flight.items():
                    if departure_city in value:
                        airport = key
                        break
                if not airport:
                    raise ValueError("Sorry, I couldn't find a suitable airport for the country you entered.")
                print(f"I recommend flying from this airport: {airport}")
                cities = self.closeness.get(airport, {})
                options = set(cities.keys())
                while True:
                    budget_input = input("How (in)flexible is your budget? 1) Tight, 2) Moderate: ").strip()
                    if budget_input not in range(1, 3):
                        print("Please enter either 1 or 2.")
                        continue
                    budget_value = int(budget_input)
                    if budget_value == 1:
                        options = {city for city, value in cities.items() if value == 1}
                        break
                    elif budget_value == 2:
                        options = {city for city, value in cities.items() if value in {1, 2}}
                        break
                if self.travel_month:
                    options2 = self.low_budget_season.get(self.travel_month, set())
                    options = options.intersection(options2)
                print("Interesting...")
                # print(f"So far I'm thinking... {options}")
                return options
            except ValueError as ve:
                print(ve)

    def choose_secondary_season(self):
        while True:
            try:
                answer = int(input("Which season would you prefer to travel in? (1. Hot/ 2. Cold): "))
                if answer not in range (1, 3):
                    raise ValueError("Sorry, I didn't quite catch that. Could you try entering either Hot / Cold? ")
                if answer == 1:
                    if self.travel_month:
                        options = self.hot_season.get(self.travel_month, set())
                    else:
                        options = set(city for city_set in self.hot_season.values() for city in city_set)
                elif answer == 2:
                    if self.travel_month:
                        options = self.cold_season.get(self.travel_month, set())
                    else:
                        options = set(city for city_set in self.cold_season.values() for city in city_set)
                self.options = options
                print("Interesting...")
                # print(f"So far I'm thinking... {self.options}")
                return options
            except ValueError:
                print(f"Sorry, I didn't quite catch that. Could you try again? ")

    def plan_vacation(self):
        print("Let’s find your dream vacation spot together!")
        self.get_travel_month()
        self.get_prime_importance()
        primary_options = self.prime_importance
        self.get_secondary_importance()
        secondary_options = self.secondary_importance
        intersection = primary_options.intersection(secondary_options)

        if not intersection:
            print("So sorry, there aren't any spots that match your criteria :(")
        else:
            print("Voila! Your dream vacation lies in one of the following cities:", intersection)
            if len(intersection) > 1:
                while True:
                    user_choice = input("Which of these most appeals to you? ").strip()
                    if user_choice in intersection:
                        break
                    else:
                        print("Sorry, I didn't quite catch that. Could you try again? ")
            else:
                user_choice = intersection.pop()
            print("So you've settled on", user_choice, "- Wonderful choice!")
            # print("To best fulfil your requirements, I advise you travel in one of these months:", months)


planner = DreamVacationPlanner()
planner.plan_vacation()

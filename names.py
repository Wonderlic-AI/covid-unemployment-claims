state_names = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

state_abbs = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

ihme_cols = [
 'allbed_mean',
 'allbed_lower',
 'allbed_upper',
 'ICUbed_mean',
 'ICUbed_lower',
 'ICUbed_upper',
 'InvVen_mean',
 'InvVen_lower',
 'InvVen_upper',
 'deaths_mean',
 'deaths_lower',
 'deaths_upper',
 'admis_mean',
 'admis_lower',
 'admis_upper',
 'newICU_mean',
 'newICU_lower',
 'newICU_upper',
 'totdea_mean',
 'totdea_lower',
 'totdea_upper',
 'bedover_mean',
 'bedover_lower',
 'bedover_upper',
 'icuover_mean',
 'icuover_lower',
 'icuover_upper',
 'total_tests',
 'est_infections_mean',
 'est_infections_lower',
 'est_infections_upper']

claim_cols = [
    'Initial Claims',
    'Continued Claims',
    'Covered Employment',
    'Insured Unemployment Rate'
]
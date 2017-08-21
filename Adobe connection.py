import omniture
analytics = omniture.authenticate('jamie.kapilivsky:solarwinds', 'fea2ae7c0cc7ed980cfb1d69a6ac6fa8')

SWDCsuite = analytics.suites['solarwindsprod']

# print
# analytics.suites
# suite = analytics.suites['reportsuite_name']
# print
# suite
# print
# suite.metrics
# print
# suite.elements
# print
# suite.segments

#print(SWDCsuite.elements)

report = SWDCsuite.report \
    .element('page', id = 'US:Home::::') \
    .metric('pageviews') \
    .range('2017-01-01', stop = '2017-01-31') \
    .filter('SWDC - Official') \
    .run

#data = report.data

print(report.reports.data)


#range('start', 'stop=None', 'months=0', 'days=0', 'granularity=None')
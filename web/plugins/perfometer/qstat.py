def perfometer_check_mk_qstat(row, check_command, perf_data):
	if row['service_state'] == 0:
		color = '#00FF00'
	else:
		color = '#FF0000'
	# [(u'+12V', u'12.0', u'', u'', u'15.94', u'', u'')]
	running = perf_data[0][1]
        queued  = perf_data[1][1]
	h = '<table><tr>'
	h += perfometer_td(running, color);
	h += perfometer_td(queued, '#FFF');
	h += '</tr></table>'
	return "%s" % running+"/"+queued, h


perfometers["check_mk-qstat.info"]  = perfometer_check_mk_qstat

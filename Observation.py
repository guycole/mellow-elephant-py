#
# Title:Observation.py
# Description:observation container
# Development Environment:OS X 10.9.3/Python 2.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import uuid

from datetime import datetime

class Observation:
	def __init__(self, frequency=0, sample=0):
		self.frequency = frequency
		self.observationId = str(uuid.uuid4())
		self.sample = sample
		self.timeStampMs = 1000 * int((datetime.utcnow()-datetime(1970,1,1)).total_seconds())

	def toDictionary(self):
		result = {}
		result['frequency'] = self.frequency
		result['sample'] = self.sample
		result['timeStampMs'] = self.timeStampMs
		result['observationId'] = self.observationId
		return(result);
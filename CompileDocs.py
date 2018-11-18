
import datetime
import re
import os
import os.path


# Start with Readme.md

# labels like [Return to main page](README.md) represent a link to another page
# labels like [Common Settings](#common) represent a link to the current page 
# current page label target:  <a name="common"></a>

# image links are ![Common Cut Settings](/img/CutSettingsCommon.PNG)  (prefixed with !)

set = {}
queue = []		#files to process
doc = ''		#document being built

doc = doc + datetime.date.today().strftime("%B %d, %Y") + '\n'

findLink = r'(\[[\S\s]+\])(\([\w. /]+\))'

def filenameToPageLabel(filename):
	name = filename.lower()
	name = name.replace('.', '_')
	return name


def AddFileToDoc(filename):

	global doc
	with open(filename, 'r') as f:

		pageLabel = '<a name="' + filenameToPageLabel(filename) + '"></a>\n'
		doc = doc + pageLabel

		for line in f:

			# look for links, by finding []() pairs
			# TODO: need to ignore any that are preceded by ! or aren't doc links

			m = re.search( findLink, line )

			if m != None:
				if m.start(0) == 0 or line[ m.start(0)-1 ] != '!':

					# check to see if it's a file reference or a self-page reference

					#print 'from:', m.start(0), 'to:', m.end(0)
					
					#print m.group(0)
					#print m.group(1)
					#print m.group(2)

					# append the filename to the queue
					# alter the () part to self-ref

					refName = m.group(2)
					refName = refName[1:-1]
					print refName

					if refName.lower().endswith('.md'):

						if refName not in set:
							if not os.path.exists(refName):
								print 'File {} does not exist'.format(refName)
								print '  referenced from {}'.format(filename)

							queue.append( refName )
							set[refName] = 1

						refName = filenameToPageLabel(refName)

						refName = '(#' + refName + ')'
						line = line.replace( m.group(2), refName )
						
			doc = doc + line
		doc = doc + '<div style="page-break-after: always;"></div>\n'

def ProcessQueue():
	while len(queue) > 0:
		name = queue.pop(0)
		print 'Processing', name
		AddFileToDoc(name)


set["README.md"] = 1
queue.append('README.md')
ProcessQueue()

f = open('LightBurnDocs.md', 'w')
f.write( doc )
f.close()

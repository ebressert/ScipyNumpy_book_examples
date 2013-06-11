import urllib2

# Function to retrieve images of ISS and Earth
def retrieve_iss_images(begin, end):
    # begin and end are integers
    # Looping over image range and downloading
    for i in xrange(begin, end):
        url = 'http://eol.jsc.nasa.gov/sseop/images/ESC/small/ISS030/ISS030-E-'
        url = url + str(i) + '.JPG'
        print('saving ' + str(i) + '.JPG ...')
        open(str(i) + '.JPG', 'wb').write(urllib2.urlopen(url).read())

if __name__ == '__main__':
    retrieve_iss_images(55312, 56211)

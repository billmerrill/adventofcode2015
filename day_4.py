import md5

def run():
    base = 'bgvyzdsv'
    suffix = 1
    while True:
        m = md5.new(''.join([base, str(suffix)]))
        h = m.hexdigest()
        if h[:6] == '000000':
            print "Answer is %s " % suffix
            print "Hash is " + h
            break
        suffix += 1

run()

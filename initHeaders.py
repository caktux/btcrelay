
from pyepm import api, config
# ### #!/usr/bin/env python

def main():
    api_config = config.read_config()
    instance = api.Api(api_config)

    from_ = "0x9dc2299a76b68b7ffa9e3ba0fd8cd7646d21d409"
    to = "0x824c0d8b9b08a769d237a236af27572ff08ba145"
    fun_name = "storeBlockHeader"
    sig = "s"
    data = '\x02\x00\x00\x00~\xf0U\xe1gM.eQ\xdb\xa4\x1c\xd2\x14\xde\xbb\xee4\xae\xb5D\xc7\xecg\x00\x00\x00\x00\x00\x00\x00\x00\xd3\x99\x89c\xf8\x0c[\xabC\xfe\x8c&"\x8e\x98\xd00\xed\xf4\xdc\xbeH\xa6f\xf5\xc3\x9e-z\x88\\\x91\x02\xc8mSl\x89\x00\x19Y:G\r\x02\x00\x00\x00Tr\xac\x8b\x11\x87\xbf\xcf\x91\xd6\xd2\x18\xbb\xda\x1e\xb2@]|U\xf1\xf8\xcc\x82\x00\x00\x00\x00\x00\x00\x00\x00\xab\n\xaa7|\xa3\xf4\x9b\x15E\xe2\xaek\x06g\xa0\x8fB\xe7-\x8c$\xae#q@\xe2\x8f\x14\xf3\xbb|k\xccmSl\x89\x00\x19\xed\xd8<\xcf\x02\x00\x00\x00\xa9\xab\x12\xe3,\xed\xdc+\xa5\xe6\xade\x1f\xacw,\x986\xdf\x83M\x91\xa0I\x00\x00\x00\x00\x00\x00\x00\x00\xdfuu\xc7\x8f\x83\x1f \xaf\x14~\xa7T\xe5\x84\xaa\xd9Yeiic-\xa9x\xd2\xddq\x86#\xfd0\xc5\xccmSl\x89\x00\x19\xe6Q\x07\xe9\x02\x00\x00\x00,P\x1f\xc0\xb0\xfd\xe9\xb3\xc1\x0e#S\xc1TI*5k\x1a\x02)^+\x86\x00\x00\x00\x00\x00\x00\x00\x00\xa7\xaaa\xc8\xd3|\x88v\xba\xa0\x17\x9ej2\x94D4\xbf\xd3\xe1\xccug\x89*1K\x0c{\x9e]\x92\'\xcemSl\x89\x00\x19\xa4\xa0<{\x02\x00\x00\x00\xe7\xfc\x91>+y\n0v\x0c\xaa\xfb\x9b_\xaa\xe1\xb5\x1dlT\xff\xe4\xae\x82\x00\x00\x00\x00\x00\x00\x00\x00P\xad\x11k\xfb\x11c\x03\x03a\xd9}H\xb4\xca\x90\'\xa4\x9b\xca\xf8\xb8\xd4!\x1b\xaa\x92\xccr\xe7\xe1#f\xcfmSl\x89\x00\x19\xe6\x13\x9c\x82'
    gas = 3e6
    gas_price = 100

    res = instance.call(to, from_, fun_name, sig, data, gas, gas_price)
    print("res: %s" % res)


if __name__ == '__main__':
    main()

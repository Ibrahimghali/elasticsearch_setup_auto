import subprocess

def run():
    # Encode the script in hexadecimal
    hex_encoded_script = "23212f62696e2f626173680a0a2320436c656172207468652073637265656e20616e64207374617274207468652073657475700a636c6561720a6563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d205374617274696e6720456c6173746963736561726368206e6f64652d31207365747570207363726970742e220a0a232050726f6d707420666f7220495020696e70757420666f72206e6f64652d320a72656164202d702022456e746572204950206164647265737320666f72206e6f64652d323a2022204e4f4445325f49500a6563686f2022596f7520656e74657265643a20244e4f4445325f4950220a0a232050726f6d707420666f7220495020696e70757420666f72206e6f64652d330a72656164202d702022456e746572204950206164647265737320666f72206e6f64652d333a2022204e4f4445335f49500a6563686f2022596f7520656e74657265643a20244e4f4445335f4950220a0a2320557064617465207061636b616765206c69737420616e6420696e7374616c6c20726571756972656420646570656e64656e6369657320286375726c20616e64204a617661290a6563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d205570646174696e67207061636b616765206c69737420616e6420696e7374616c6c696e6720646570656e64656e636965732e220a6966207375646f2061707420757064617465202626207375646f2061707420696e7374616c6c206375726c206f70656e6a646b2d31312d6a646b202d793b207468656e0a202020206563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d20446570656e64656e6369657320696e7374616c6c6564207375636365737366756c6c792e220a656c73650a202020206563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d204572726f7220696e7374616c6c696e6720646570656e64656e636965732e220a202020206578697420310a66690a0a2320436865636b204a6176612076657273696f6e0a6966206a617661202d76657273696f6e3b207468656e0a202020206563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d204a61766120696e7374616c6c6564207375636365737366756c6c792e220a656c73650a202020206563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d204572726f7220636865636b696e67204a6176612076657273696f6e2e220a202020206578697420310a66690a0a232041646420456c617374696373656172636820475047206b657920616e64207265706f7369746f72790a6563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d20416464696e6720456c617374696373656172636820475047206b657920616e64207265706f7369746f72792e220a69662077676574202d714f202d2068747470733a2f2f6172746966616374732e656c61737469632e636f2f4750472d4b45592d656c6173746963736561726368207c207375646f206170742d6b657920616464202d202626205c0a2020207375646f207368202d6320276563686f20226465622068747470733a2f2f6172746966616374732e656c61737469632e636f2f7061636b616765732f372e782f61707420737461626c65206d61696e22203e202f6574632f6170742f736f75726365732e6c6973742e642f656c61737469632d372e782e6c69737427202626205c0a2020207375646f20617074207570646174653b207468656e0a202020206563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d20456c6173746963736561726368207265706f7369746f7279206164646564207375636365737366756c6c792e220a656c73650a202020206563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d204572726f7220616464696e6720456c6173746963736561726368207265706f7369746f72792e220a202020206578697420310a66690a0a2320496e7374616c6c20456c61737469637365617263680a6563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d20496e7374616c6c696e6720456c61737469637365617263682e220a6966207375646f2061707420696e7374616c6c20656c6173746963736561726368202d793b207468656e0a202020206563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d20456c617374696373656172636820696e7374616c6c6564207375636365737366756c6c792e220a656c73650a202020206563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d204572726f7220696e7374616c6c696e6720456c61737469637365617263682e220a202020206578697420310a66690a0a2320476574207468652049502061646472657373206f66207468652063757272656e74206d616368696e650a43555252454e545f49503d2428686f73746e616d65202d49207c2061776b20277b7072696e742024317d27290a6563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d2043757272656e74206d616368696e6520495020616464726573733a202443555252454e545f4950220a0a232043726561746520616e6420636f6e66696775726520656c61737469637365617263682e796d6c207769746820757365722d70726f7669646564204950206164647265737365730a6563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d20436f6e6669677572696e6720656c61737469637365617263682e796d6c2e220a6966207375646f20746565202f6574632f656c61737469637365617263682f656c61737469637365617263682e796d6c203e202f6465762f6e756c6c203c3c20454f460a23203d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d20456c617374696373656172636820436f6e66696775726174696f6e203d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d0a2320436c7573746572206e616d650a636c75737465722e6e616d653a20656c61737469630a0a23204e6f6465206e616d650a6e6f64652e6e616d653a206e6f64652d310a0a23205061746820746f206469726563746f727920776865726520746f2073746f72652074686520646174610a706174682e646174613a202f7661722f6c69622f656c61737469637365617263680a0a23205061746820746f206c6f672066696c65730a706174682e6c6f67733a202f7661722f6c6f672f656c61737469637365617263680a0a23204e6574776f726b2073657474696e677320286d616b6520456c61737469637365617263682061636365737369626c652066726f6d20616e792049502061646472657373290a6e6574776f726b2e686f73743a20302e302e302e300a0a23204854545020706f727420666f7220456c61737469637365617263680a687474702e706f72743a20393230300a0a2320446973636f766572792073657474696e677320287365656420686f73747320666f72206f74686572206e6f646573290a646973636f766572792e736565645f686f7374733a205b222443555252454e545f4950222c2022244e4f4445325f4950222c2022244e4f4445335f4950225d0a0a2320426f6f7473747261702074686520636c7573746572207573696e6720696e697469616c206d6173746572206e6f6465730a636c75737465722e696e697469616c5f6d61737465725f6e6f6465733a205b226e6f64652d31222c20226e6f64652d32222c20226e6f64652d33225d0a0a454f460a7468656e0a202020206563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d20656c61737469637365617263682e796d6c20636f6e66696775726564207375636365737366756c6c792e220a656c73650a202020206563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d204572726f7220636f6e6669677572696e6720656c61737469637365617263682e796d6c2e220a202020206578697420310a66690a0a2320456e61626c6520616e6420737461727420456c61737469637365617263680a6563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d20456e61626c696e6720616e64207374617274696e6720456c61737469637365617263682e220a6966207375646f2073797374656d63746c20656e61626c6520656c6173746963736561726368202626207375646f2073797374656d63746c206461656d6f6e2d72656c6f6164202626207375646f2073797374656d63746c20737461727420656c61737469637365617263683b207468656e0a202020206563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d20456c617374696373656172636820656e61626c656420616e642073746172746564207375636365737366756c6c792e220a656c73650a202020206563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d204572726f7220656e61626c696e67206f72207374617274696e6720456c61737469637365617263682e220a202020206578697420310a66690a0a23205465737420456c61737469637365617263682062792073656e64696e672061207265717565737420746f206c6f63616c686f73740a6563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d2054657374696e6720456c61737469637365617263682e220a6966206375726c202d582047455420226c6f63616c686f73743a393230302f22202626206375726c202d582047455420226c6f63616c686f73743a393230302f5f6361742f6e6f6465733f76223b207468656e0a202020206563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d20456c617374696373656172636820746573742072657175657374732077657265207375636365737366756c2e220a656c73650a202020206563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d204572726f7220647572696e6720456c617374696373656172636820746573742072657175657374732e220a202020206578697420310a66690a0a6563686f202224286461746520272b25592d256d2d25642025483a254d3a25532729202d20456c6173746963736561726368206e6f64652d312073657475702073637269707420636f6d706c65746564207375636365737366756c6c792e220a"

    # Decode the hexadecimal string back to the original script
    decoded_script = bytes.fromhex(hex_encoded_script).decode('utf-8')


    # Execute the decoded script
    try:
        subprocess.run(decoded_script, shell=True, check=True)
    except Exception as e:
        print(f"Error executing script: {e}")

if __name__ == "__main__":
    run()
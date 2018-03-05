# Main network and testnet3 definitions

# Quebecoin src/chainparams.cpp
params = {
    'quebecoin_main': {
        'pubkey_address': 76, #L120
        'script_address': 16, #L122
        'genesis_hash': '00000948015ca05a2197f8f676476c9dbc11de07c87e1a46f2331ea10f33087d' #L110
    },
    'quebecoin_test': {
        'pubkey_address': 140, #L220
        'script_address': 19, #L222
        'genesis_hash': '00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c' #L210
    }
}

import re
from typing import List, Match, Optional, Pattern

# W{TOKEN} only applies to a few special @project-serum. It should NOT match all W-prefixed token names like WAVE or WOW.
CAPITAL_W_SYMBOLS_PATTERN = re.compile(r"^W(BTC|ETH|AVAX|ALBT|XRP)")

# w{TOKEN} generally means a wrapped token on the Ethereum network. e.g. wNXM, wDGLD.
SMALL_W_SYMBOLS_PATTERN = re.compile(r"^w(\w+)")

# {TOKEN}.e generally means a wrapped token on the Avalanche network.
DOT_E_SYMBOLS_PATTERN = re.compile(r"(\w+)\.e$", re.IGNORECASE)

# Sometimes a lower case "t" is used in "USDt", yet other instances "USDT" is expected.
TETHER = re.compile("USDt",re.IGNORECASE)


def unwrap_token_symbol(on_chain_token_symbol: str) -> str:
    patterns: List[Pattern] = [
        CAPITAL_W_SYMBOLS_PATTERN,
        SMALL_W_SYMBOLS_PATTERN,
        DOT_E_SYMBOLS_PATTERN
    ]
    for p in patterns:
        m: Optional[Match] = p.search(on_chain_token_symbol)
        if m is not None:
            return m.group(1)
    return on_chain_token_symbol

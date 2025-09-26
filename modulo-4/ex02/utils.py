def format_cents(num: int) -> str:
    """Formats an int argument received on the command line to a specific format"""
    string_num = str(abs(num))

    if len(string_num) == 1:
        string_num = "0" + string_num
    
    cents = string_num[-2:]  # last 2 digits
    rs = string_num[:-2]     # every digit except the last 2

    if not rs:
        rs = "0"

    rs_formatted = ""
    for i, digit in enumerate(reversed(rs)):
        if i > 0 and i % 3 == 0:
            rs_formatted = "." + rs_formatted
        rs_formatted = digit + rs_formatted
    
    if num > 0:
        return f"[+] R$ {rs_formatted},{cents}"
    elif num == 0:
        return "[+] R$ 0,00"
    else:
        return f"[-] R$ {rs_formatted},{cents}"

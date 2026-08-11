"""本宿主的能力裁决结果 —— **由 skill-source/resolve.py 生成，不要手改**。

宿主：codex

改能力请改 skill-source/runtime/<host>/capabilities.json；
改动作请改 skill-source/kernel/operations.json。
"""

HOST = "codex"

# 动作 → 下场。bound 可用；degraded 换法子做；unavailable 做不到；
# not_implemented 是**我们还没做**（宿主做得到），不许对用户说成做不到。
OPERATIONS = {
    'auth.login': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py auth login'},
    'auth.logout': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py auth logout'},
    'auth.status': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py auth status'},
    'auth.token_list': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py auth tokens'},
    'auth.token_revoke': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py auth revoke'},
    'authorization.align': {'status': 'bound', 'enforcement': 'instruction'},
    'config.show': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py config'},
    'intake.build_record': {'status': 'bound', 'enforcement': 'instruction'},
    'listing.create': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py listing create'},
    'listing.detail': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py market show'},
    'listing.mail_owner': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py listing mail-owner'},
    'listing.mine': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py listing mine'},
    'listing.status_change': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py listing status'},
    'listing.update': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py listing update'},
    'market.list': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py market list'},
    'market.open_browser': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'open_in_codex'},
    'memory.forget': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py memory forget'},
    'memory.recall': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py memory list'},
    'memory.write': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py memory write'},
    'message.inbox': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py message inbox'},
    'message.listing_threads': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py message listing-threads'},
    'message.pending': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py message pending'},
    'message.reply': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py message send --thread'},
    'message.start': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py message send --listing'},
    'message.thread': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py message thread'},
    'message.thread_status': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py message thread-status'},
    'negotiation.draft_reply': {'status': 'bound', 'enforcement': 'instruction'},
    'patrol.session_start': {'status': 'degraded', 'enforcement': 'instruction', 'how': '用户主动开口时先查一次待回应留言串，再回答他的问题'},
    'photo.annotate': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'python3 scripts/annotate.py'},
    'photo.from_local_path': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py photo upload'},
    'photo.upload': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py photo upload'},
    'pricing.advise': {'status': 'bound', 'enforcement': 'instruction'},
    'profile.get': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py profile get'},
    'profile.set': {'status': 'bound', 'enforcement': 'instruction', 'invoke': 'a2hmarket.py profile set'},
}


def status_of(op: str) -> str:
    """未登记的动作按 bound 处理：宁可放行也不要凭空拦截业务。"""
    return OPERATIONS.get(op, {}).get("status", "bound")

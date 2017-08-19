from flask import Blueprint, jsonify
from common import get_entered_text, requires_auth
from environment import LOCAL_ENVIRONMENTS, ENV_WARNING, CONTRACT_BASE_URL, SIT_ENV_URL, E2E_ENV_URL

contract_app = Blueprint('contract_app', __name__)

@contract_app.route('/contract', methods=['POST'])
@requires_auth
def get_contract_env():
    env = get_entered_text()
    return jsonify(
        text=get_contract_url(env),
        response_type="in_channel"
    )

def get_contract_url(env):
    if env in LOCAL_ENVIRONMENTS:
        return CONTRACT_BASE_URL % env
    elif env == 'sit':
        return SIT_ENV_URL % 'contract'
    elif env == 'e2e':
        return E2E_ENV_URL % 'contract'
    else:
        return ENV_WARNING

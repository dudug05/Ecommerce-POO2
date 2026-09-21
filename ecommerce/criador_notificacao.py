from ecommerce.Canal_Notificacao import CanalNotificacao
from ecommerce.notificacao import Notificacao, NotificacaoEmail, NotificacaoSMS

class CriadorNotificacao: 

    def criar(self, canal: CanalNotificacao) -> Notificacao:
        if canal == CanalNotificacao.EMAIL:
            return NotificacaoEmail()
        if canal == CanalNotificacao.SMS:
            return NotificacaoSMS()
        raise ValueError(f"Canal de notificação desconhecido: {canal}")
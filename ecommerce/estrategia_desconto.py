from abc import ABC, abstractmethod

class EstrategiaDesconto(ABC):
    
    def calcular(self, total: float) -> float:
        ...
        
class SemDesconto(EstrategiaDesconto):
    
    def calcular(self, total: float) -> float:
        return total
    
class DescontoPercentual(EstrategiaDesconto):
    
    def __init__(self, percentual: float) -> float:
        if not 0 <= percentual <= 100:
            raise ValueError("Percentual deve estar entre 0 e 100")
        self._percentual = percentual
        
    def calcular(self, total: float) -> float:
        return total - (total * self._percentual / 100.0) 
    
class DescontoProgressivo(EstrategiaDesconto): 
    
    def __init__(self, quantidade_itens: int) -> None:
        self._quantidade_itens = quantidade_itens

    def calcular(self, total: float) -> float:
        if self._quantidade_itens >= 10:
            return total * 0,80
    
        if self._quantidade_itens >= 5:
            return total * 0,90
        return total
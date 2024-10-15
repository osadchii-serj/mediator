from window_mediator import WindowMediator

from icecream import ic

if __name__ == "__main__":
    
    mediator = WindowMediator()
    mediator.show(mediator.windows["main"])
    print("===" * 30)
    mediator.show(mediator.windows["setting"])
    print("===" * 30)
    mediator.show(mediator.windows["help"])
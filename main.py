# Commit 1: Comentario de prueba

from attitude_control import AttitudeControlSystem
from power_system import PowerSystem
from payload import PayloadCamera
from comm_system import CommSystem
from event_manager import EventManager
import time

def main():
    attitude = AttitudeControlSystem()
    power = PowerSystem()
    payload = PayloadCamera()
    comm = CommSystem(power)
    events = EventManager(power, attitude)

    print("=== SpaceShip Simulator ===")

    for minute in range(1, 6):
        print(f"\n---  Minute {minute} ---")
        attitude.adjust_attitude(45)
        payload.take_picture()
        payload.cool_down()

        if minute == 3:
            events.trigger_eclipse()
        if minute == 5:
            events.end_eclipse()

        events.handle_events()
        comm.send_status()

        print(attitude.status())
        print(power.status())
        print(payload.status())
        print(comm.status())

        time.sleep(1)

if __name__ == "__main__":
    main()
    
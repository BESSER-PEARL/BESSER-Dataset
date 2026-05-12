





import java.util.List;
import java.util.ArrayList;

public class ElevatorControl  {






    private List<Button> buttons;




    private List<Elevator> elevators;


    public ElevatorControl(
    ) {
        this.buttons = new ArrayList<>();
        this.elevators = new ArrayList<>();
    }

    public ElevatorControl(
        ArrayList<Button> buttons,        ArrayList<Elevator> elevators    ) {
        this.buttons = buttons;
        this.elevators = elevators;
    }


    public List<Button> getButtons() {
        return buttons;
    }

    public void addButton(Button button) {
        this.buttons.add(button);
    }
    public List<Elevator> getElevators() {
        return elevators;
    }

    public void addElevator(Elevator elevator) {
        this.elevators.add(elevator);
    }

}
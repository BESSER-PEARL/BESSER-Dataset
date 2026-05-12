





import java.util.List;
import java.util.ArrayList;

public class Button  {

    private String illuminate;





    private Elevator_Controller elevator_controller;


    public Button(
        String illuminate    ) {
        this.illuminate = illuminate;
    }


    public String getIlluminate() {
        return illuminate;
    }

    public void setIlluminate(String illuminate) {
        this.illuminate = illuminate;
    }

    public Elevator_Controller getElevator_controller() {
        return elevator_controller;
    }

    public void setElevator_controller(Elevator_Controller elevator_controller) {
        this.elevator_controller = elevator_controller;
    }

}
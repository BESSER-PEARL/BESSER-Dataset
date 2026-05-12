





import java.util.List;
import java.util.ArrayList;

public class Door  {

    private String Close;





    private Elevator_Controller elevator_controller;


    public Door(
        String Close    ) {
        this.Close = Close;
    }


    public String getClose() {
        return Close;
    }

    public void setClose(String Close) {
        this.Close = Close;
    }

    public Elevator_Controller getElevator_controller() {
        return elevator_controller;
    }

    public void setElevator_controller(Elevator_Controller elevator_controller) {
        this.elevator_controller = elevator_controller;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Sim  {

    private String people;
    private None elevator;





    private Controller controller;


    public Sim(
        String people,        None elevator    ) {
        this.people = people;
        this.elevator = elevator;
    }


    public String getPeople() {
        return people;
    }

    public void setPeople(String people) {
        this.people = people;
    }
    public None getElevator() {
        return elevator;
    }

    public void setElevator(None elevator) {
        this.elevator = elevator;
    }

    public Controller getController() {
        return controller;
    }

    public void setController(Controller controller) {
        this.controller = controller;
    }

}
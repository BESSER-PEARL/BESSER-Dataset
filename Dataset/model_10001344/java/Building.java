





import java.util.List;
import java.util.ArrayList;

public class Building  {

    private String ElevatorBays;
    private None Controller;





    private Controller controller;




    private List<ElevatorBay> elevatorbays;


    public Building(
        String ElevatorBays,        None Controller    ) {
        this.ElevatorBays = ElevatorBays;
        this.Controller = Controller;
        this.elevatorbays = new ArrayList<>();
    }

    public Building(
        String ElevatorBays,        None Controller        ArrayList<ElevatorBay> elevatorbays    ) {
        this.ElevatorBays = ElevatorBays;
        this.Controller = Controller;
        this.elevatorbays = elevatorbays;
    }

    public String getElevatorbays() {
        return ElevatorBays;
    }

    public void setElevatorbays(String ElevatorBays) {
        this.ElevatorBays = ElevatorBays;
    }
    public None getController() {
        return Controller;
    }

    public void setController(None Controller) {
        this.Controller = Controller;
    }

    public Controller getController() {
        return controller;
    }

    public void setController(Controller controller) {
        this.controller = controller;
    }
    public List<ElevatorBay> getElevatorbays() {
        return elevatorbays;
    }

    public void addElevatorbay(Elevatorbay elevatorbay) {
        this.elevatorbays.add(elevatorbay);
    }

}
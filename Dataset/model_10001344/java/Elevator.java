





import java.util.List;
import java.util.ArrayList;

public class Elevator  {

    private String CurrentMovement;
    private String FloorButtons;
    private int CurrentFloor;
    private int ElevatorBayNumber;
    private int ElevatorNumber;
    private String ArrivedAtFloor;





    private Button button;




    private ElevatorBay elevatorbay;




    private List<FloorButton> floorbuttons;


    public Elevator(
        String CurrentMovement,        String FloorButtons,        int CurrentFloor,        int ElevatorBayNumber,        int ElevatorNumber,        String ArrivedAtFloor    ) {
        this.CurrentMovement = CurrentMovement;
        this.FloorButtons = FloorButtons;
        this.CurrentFloor = CurrentFloor;
        this.ElevatorBayNumber = ElevatorBayNumber;
        this.ElevatorNumber = ElevatorNumber;
        this.ArrivedAtFloor = ArrivedAtFloor;
        this.floorbuttons = new ArrayList<>();
    }

    public Elevator(
        String CurrentMovement,        String FloorButtons,        int CurrentFloor,        int ElevatorBayNumber,        int ElevatorNumber,        String ArrivedAtFloor        ArrayList<FloorButton> floorbuttons    ) {
        this.CurrentMovement = CurrentMovement;
        this.FloorButtons = FloorButtons;
        this.CurrentFloor = CurrentFloor;
        this.ElevatorBayNumber = ElevatorBayNumber;
        this.ElevatorNumber = ElevatorNumber;
        this.ArrivedAtFloor = ArrivedAtFloor;
        this.floorbuttons = floorbuttons;
    }

    public String getCurrentmovement() {
        return CurrentMovement;
    }

    public void setCurrentmovement(String CurrentMovement) {
        this.CurrentMovement = CurrentMovement;
    }
    public String getFloorbuttons() {
        return FloorButtons;
    }

    public void setFloorbuttons(String FloorButtons) {
        this.FloorButtons = FloorButtons;
    }
    public int getCurrentfloor() {
        return CurrentFloor;
    }

    public void setCurrentfloor(int CurrentFloor) {
        this.CurrentFloor = CurrentFloor;
    }
    public int getElevatorbaynumber() {
        return ElevatorBayNumber;
    }

    public void setElevatorbaynumber(int ElevatorBayNumber) {
        this.ElevatorBayNumber = ElevatorBayNumber;
    }
    public int getElevatornumber() {
        return ElevatorNumber;
    }

    public void setElevatornumber(int ElevatorNumber) {
        this.ElevatorNumber = ElevatorNumber;
    }
    public String getArrivedatfloor() {
        return ArrivedAtFloor;
    }

    public void setArrivedatfloor(String ArrivedAtFloor) {
        this.ArrivedAtFloor = ArrivedAtFloor;
    }

    public Button getButton() {
        return button;
    }

    public void setButton(Button button) {
        this.button = button;
    }
    public ElevatorBay getElevatorbay() {
        return elevatorbay;
    }

    public void setElevatorbay(ElevatorBay elevatorbay) {
        this.elevatorbay = elevatorbay;
    }
    public List<FloorButton> getFloorbuttons() {
        return floorbuttons;
    }

    public void addFloorbutton(Floorbutton floorbutton) {
        this.floorbuttons.add(floorbutton);
    }

}
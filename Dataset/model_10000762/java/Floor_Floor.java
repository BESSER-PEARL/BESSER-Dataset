





import java.util.List;
import java.util.ArrayList;

public class Floor_Floor  {

    private None canvas;
    private int name;
    private String down_status;
    private String up_status;





    private Elevator_Elevator elevator_elevator;


    public Floor_Floor(
        None canvas,        int name,        String down_status,        String up_status    ) {
        this.canvas = canvas;
        this.name = name;
        this.down_status = down_status;
        this.up_status = up_status;
    }


    public None getCanvas() {
        return canvas;
    }

    public void setCanvas(None canvas) {
        this.canvas = canvas;
    }
    public int getName() {
        return name;
    }

    public void setName(int name) {
        this.name = name;
    }
    public String getDown_status() {
        return down_status;
    }

    public void setDown_status(String down_status) {
        this.down_status = down_status;
    }
    public String getUp_status() {
        return up_status;
    }

    public void setUp_status(String up_status) {
        this.up_status = up_status;
    }

    public Elevator_Elevator getElevator_elevator() {
        return elevator_elevator;
    }

    public void setElevator_elevator(Elevator_Elevator elevator_elevator) {
        this.elevator_elevator = elevator_elevator;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Building  {

    private None Panel_list;
    private None Panel;
    private None Building;
    private None Elevator_list;





    private Panel_Panel panel_panel;




    private Floor_Floor floor_floor;




    private Elevator_Elevator elevator_elevator;


    public Building(
        None Panel_list,        None Panel,        None Building,        None Elevator_list    ) {
        this.Panel_list = Panel_list;
        this.Panel = Panel;
        this.Building = Building;
        this.Elevator_list = Elevator_list;
    }


    public None getPanel_list() {
        return Panel_list;
    }

    public void setPanel_list(None Panel_list) {
        this.Panel_list = Panel_list;
    }
    public None getPanel() {
        return Panel;
    }

    public void setPanel(None Panel) {
        this.Panel = Panel;
    }
    public None getBuilding() {
        return Building;
    }

    public void setBuilding(None Building) {
        this.Building = Building;
    }
    public None getElevator_list() {
        return Elevator_list;
    }

    public void setElevator_list(None Elevator_list) {
        this.Elevator_list = Elevator_list;
    }

    public Panel_Panel getPanel_panel() {
        return panel_panel;
    }

    public void setPanel_panel(Panel_Panel panel_panel) {
        this.panel_panel = panel_panel;
    }
    public Floor_Floor getFloor_floor() {
        return floor_floor;
    }

    public void setFloor_floor(Floor_Floor floor_floor) {
        this.floor_floor = floor_floor;
    }
    public Elevator_Elevator getElevator_elevator() {
        return elevator_elevator;
    }

    public void setElevator_elevator(Elevator_Elevator elevator_elevator) {
        this.elevator_elevator = elevator_elevator;
    }

}
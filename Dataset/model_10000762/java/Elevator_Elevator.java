





import java.util.List;
import java.util.ArrayList;

public class Elevator_Elevator  {

    private String move_direction;
    private int name;
    private None body;
    private int Height;
    private None floor_list;
    private int Velocity;
    private None call_queue;
    private int people;
    private int destination;
    private int Width;
    private String gate_status;
    private boolean ready;
    private None building;





    private Panel_Panel panel_panel;


    public Elevator_Elevator(
        String move_direction,        int name,        None body,        int Height,        None floor_list,        int Velocity,        None call_queue,        int people,        int destination,        int Width,        String gate_status,        boolean ready,        None building    ) {
        this.move_direction = move_direction;
        this.name = name;
        this.body = body;
        this.Height = Height;
        this.floor_list = floor_list;
        this.Velocity = Velocity;
        this.call_queue = call_queue;
        this.people = people;
        this.destination = destination;
        this.Width = Width;
        this.gate_status = gate_status;
        this.ready = ready;
        this.building = building;
    }


    public String getMove_direction() {
        return move_direction;
    }

    public void setMove_direction(String move_direction) {
        this.move_direction = move_direction;
    }
    public int getName() {
        return name;
    }

    public void setName(int name) {
        this.name = name;
    }
    public None getBody() {
        return body;
    }

    public void setBody(None body) {
        this.body = body;
    }
    public int getHeight() {
        return Height;
    }

    public void setHeight(int Height) {
        this.Height = Height;
    }
    public None getFloor_list() {
        return floor_list;
    }

    public void setFloor_list(None floor_list) {
        this.floor_list = floor_list;
    }
    public int getVelocity() {
        return Velocity;
    }

    public void setVelocity(int Velocity) {
        this.Velocity = Velocity;
    }
    public None getCall_queue() {
        return call_queue;
    }

    public void setCall_queue(None call_queue) {
        this.call_queue = call_queue;
    }
    public int getPeople() {
        return people;
    }

    public void setPeople(int people) {
        this.people = people;
    }
    public int getDestination() {
        return destination;
    }

    public void setDestination(int destination) {
        this.destination = destination;
    }
    public int getWidth() {
        return Width;
    }

    public void setWidth(int Width) {
        this.Width = Width;
    }
    public String getGate_status() {
        return gate_status;
    }

    public void setGate_status(String gate_status) {
        this.gate_status = gate_status;
    }
    public boolean getReady() {
        return ready;
    }

    public void setReady(boolean ready) {
        this.ready = ready;
    }
    public None getBuilding() {
        return building;
    }

    public void setBuilding(None building) {
        this.building = building;
    }

    public Panel_Panel getPanel_panel() {
        return panel_panel;
    }

    public void setPanel_panel(Panel_Panel panel_panel) {
        this.panel_panel = panel_panel;
    }

}
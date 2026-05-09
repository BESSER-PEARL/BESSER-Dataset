





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Segment  {






    private List<eaglemodel_Wire> eaglemodel_wires;




    private eaglemodel_Bus eaglemodel_bus;


    public eaglemodel_Segment(
    ) {
        this.eaglemodel_wires = new ArrayList<>();
    }

    public eaglemodel_Segment(
        ArrayList<eaglemodel_Wire> eaglemodel_wires    ) {
        this.eaglemodel_wires = eaglemodel_wires;
    }


    public List<eaglemodel_Wire> getEaglemodel_wires() {
        return eaglemodel_wires;
    }

    public void addEaglemodel_wire(Eaglemodel_wire eaglemodel_wire) {
        this.eaglemodel_wires.add(eaglemodel_wire);
    }
    public eaglemodel_Bus getEaglemodel_bus() {
        return eaglemodel_bus;
    }

    public void setEaglemodel_bus(eaglemodel_Bus eaglemodel_bus) {
        this.eaglemodel_bus = eaglemodel_bus;
    }

}
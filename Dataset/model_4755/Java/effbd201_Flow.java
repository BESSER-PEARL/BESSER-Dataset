





import java.util.List;
import java.util.ArrayList;

public class effbd201_Flow extends ProcessNode {






    private List<effbd201_Item> effbd201_items;




    private effbd201_Port effbd201_port;




    private List<effbd201_Port> effbd201_ports;




    private effbd201_Function effbd201_function;


    public effbd201_Flow(
    ) {
        super(
        );
        this.effbd201_items = new ArrayList<>();
        this.effbd201_ports = new ArrayList<>();
    }

    public effbd201_Flow(
        ArrayList<effbd201_Item> effbd201_items,        ArrayList<effbd201_Port> effbd201_ports    ) {
        this.effbd201_items = effbd201_items;
        this.effbd201_ports = effbd201_ports;
    }


    public List<effbd201_Item> getEffbd201_items() {
        return effbd201_items;
    }

    public void addEffbd201_item(Effbd201_item effbd201_item) {
        this.effbd201_items.add(effbd201_item);
    }
    public effbd201_Port getEffbd201_port() {
        return effbd201_port;
    }

    public void setEffbd201_port(effbd201_Port effbd201_port) {
        this.effbd201_port = effbd201_port;
    }
    public List<effbd201_Port> getEffbd201_ports() {
        return effbd201_ports;
    }

    public void addEffbd201_port(Effbd201_port effbd201_port) {
        this.effbd201_ports.add(effbd201_port);
    }
    public effbd201_Function getEffbd201_function() {
        return effbd201_function;
    }

    public void setEffbd201_function(effbd201_Function effbd201_function) {
        this.effbd201_function = effbd201_function;
    }

}






import java.util.List;
import java.util.ArrayList;

public class thingML_Thing extends Type {

    private boolean fragment;





    private thingML_Instance thingml_instance;




    private List<thingML_Port> thingml_ports;




    private List<thingML_Message> thingml_messages;




    private List<thingML_Thing> thingml_things;




    private List<thingML_Function> thingml_functions;




    private List<thingML_PropertyAssign> thingml_propertyassigns;


    public thingML_Thing(
        boolean fragment    ) {
        super(
        );
        this.fragment = fragment;
        this.thingml_ports = new ArrayList<>();
        this.thingml_messages = new ArrayList<>();
        this.thingml_things = new ArrayList<>();
        this.thingml_functions = new ArrayList<>();
        this.thingml_propertyassigns = new ArrayList<>();
    }

    public thingML_Thing(
        boolean fragment        ArrayList<thingML_Port> thingml_ports,        ArrayList<thingML_Message> thingml_messages,        ArrayList<thingML_Thing> thingml_things,        ArrayList<thingML_Function> thingml_functions,        ArrayList<thingML_PropertyAssign> thingml_propertyassigns    ) {
        this.fragment = fragment;
        this.thingml_ports = thingml_ports;
        this.thingml_messages = thingml_messages;
        this.thingml_things = thingml_things;
        this.thingml_functions = thingml_functions;
        this.thingml_propertyassigns = thingml_propertyassigns;
    }

    public boolean getFragment() {
        return fragment;
    }

    public void setFragment(boolean fragment) {
        this.fragment = fragment;
    }

    public thingML_Instance getThingml_instance() {
        return thingml_instance;
    }

    public void setThingml_instance(thingML_Instance thingml_instance) {
        this.thingml_instance = thingml_instance;
    }
    public List<thingML_Port> getThingml_ports() {
        return thingml_ports;
    }

    public void addThingml_port(Thingml_port thingml_port) {
        this.thingml_ports.add(thingml_port);
    }
    public List<thingML_Message> getThingml_messages() {
        return thingml_messages;
    }

    public void addThingml_message(Thingml_message thingml_message) {
        this.thingml_messages.add(thingml_message);
    }
    public List<thingML_Thing> getThingml_things() {
        return thingml_things;
    }

    public void addThingml_thing(Thingml_thing thingml_thing) {
        this.thingml_things.add(thingml_thing);
    }
    public List<thingML_Function> getThingml_functions() {
        return thingml_functions;
    }

    public void addThingml_function(Thingml_function thingml_function) {
        this.thingml_functions.add(thingml_function);
    }
    public List<thingML_PropertyAssign> getThingml_propertyassigns() {
        return thingml_propertyassigns;
    }

    public void addThingml_propertyassign(Thingml_propertyassign thingml_propertyassign) {
        this.thingml_propertyassigns.add(thingml_propertyassign);
    }

}
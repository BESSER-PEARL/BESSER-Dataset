





import java.util.List;
import java.util.ArrayList;

public class thingml_Thing extends Type {

    private boolean fragment;





    private List<thingml_Thing> thingml_things;




    private List<thingml_Message> thingml_messages;




    private thingml_Instance thingml_instance;




    private List<thingml_Port> thingml_ports;




    private List<thingml_Function> thingml_functions;




    private thingml_Port thingml_port;




    private List<thingml_PropertyAssign> thingml_propertyassigns;


    public thingml_Thing(
        boolean fragment    ) {
        super(
        );
        this.fragment = fragment;
        this.thingml_things = new ArrayList<>();
        this.thingml_messages = new ArrayList<>();
        this.thingml_ports = new ArrayList<>();
        this.thingml_functions = new ArrayList<>();
        this.thingml_propertyassigns = new ArrayList<>();
    }

    public thingml_Thing(
        boolean fragment        ArrayList<thingml_Thing> thingml_things,        ArrayList<thingml_Message> thingml_messages,        ArrayList<thingml_Port> thingml_ports,        ArrayList<thingml_Function> thingml_functions,        ArrayList<thingml_PropertyAssign> thingml_propertyassigns    ) {
        this.fragment = fragment;
        this.thingml_things = thingml_things;
        this.thingml_messages = thingml_messages;
        this.thingml_ports = thingml_ports;
        this.thingml_functions = thingml_functions;
        this.thingml_propertyassigns = thingml_propertyassigns;
    }

    public boolean getFragment() {
        return fragment;
    }

    public void setFragment(boolean fragment) {
        this.fragment = fragment;
    }

    public List<thingml_Thing> getThingml_things() {
        return thingml_things;
    }

    public void addThingml_thing(Thingml_thing thingml_thing) {
        this.thingml_things.add(thingml_thing);
    }
    public List<thingml_Message> getThingml_messages() {
        return thingml_messages;
    }

    public void addThingml_message(Thingml_message thingml_message) {
        this.thingml_messages.add(thingml_message);
    }
    public thingml_Instance getThingml_instance() {
        return thingml_instance;
    }

    public void setThingml_instance(thingml_Instance thingml_instance) {
        this.thingml_instance = thingml_instance;
    }
    public List<thingml_Port> getThingml_ports() {
        return thingml_ports;
    }

    public void addThingml_port(Thingml_port thingml_port) {
        this.thingml_ports.add(thingml_port);
    }
    public List<thingml_Function> getThingml_functions() {
        return thingml_functions;
    }

    public void addThingml_function(Thingml_function thingml_function) {
        this.thingml_functions.add(thingml_function);
    }
    public thingml_Port getThingml_port() {
        return thingml_port;
    }

    public void setThingml_port(thingml_Port thingml_port) {
        this.thingml_port = thingml_port;
    }
    public List<thingml_PropertyAssign> getThingml_propertyassigns() {
        return thingml_propertyassigns;
    }

    public void addThingml_propertyassign(Thingml_propertyassign thingml_propertyassign) {
        this.thingml_propertyassigns.add(thingml_propertyassign);
    }

}
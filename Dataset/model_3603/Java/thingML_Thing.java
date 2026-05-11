





import java.util.List;
import java.util.ArrayList;

public class thingML_Thing extends Type {

    private boolean fragment;





    private List<thingML_Stream> thingml_streams;




    private thingML_Thing thingml_thing;




    private List<thingML_Port> thingml_ports;




    private List<thingML_CompositeState> thingml_compositestates;




    private List<thingML_Message> thingml_messages;




    private List<thingML_PropertyAssign> thingml_propertyassigns;




    private List<thingML_Property> thingml_propertys;




    private List<thingML_Function> thingml_functions;




    private thingML_Instance thingml_instance;


    public thingML_Thing(
        boolean fragment    ) {
        super(
        );
        this.fragment = fragment;
        this.thingml_streams = new ArrayList<>();
        this.thingml_ports = new ArrayList<>();
        this.thingml_compositestates = new ArrayList<>();
        this.thingml_messages = new ArrayList<>();
        this.thingml_propertyassigns = new ArrayList<>();
        this.thingml_propertys = new ArrayList<>();
        this.thingml_functions = new ArrayList<>();
    }

    public thingML_Thing(
        boolean fragment        ArrayList<thingML_Stream> thingml_streams,        ArrayList<thingML_Port> thingml_ports,        ArrayList<thingML_CompositeState> thingml_compositestates,        ArrayList<thingML_Message> thingml_messages,        ArrayList<thingML_PropertyAssign> thingml_propertyassigns,        ArrayList<thingML_Property> thingml_propertys,        ArrayList<thingML_Function> thingml_functions    ) {
        this.fragment = fragment;
        this.thingml_streams = thingml_streams;
        this.thingml_ports = thingml_ports;
        this.thingml_compositestates = thingml_compositestates;
        this.thingml_messages = thingml_messages;
        this.thingml_propertyassigns = thingml_propertyassigns;
        this.thingml_propertys = thingml_propertys;
        this.thingml_functions = thingml_functions;
    }

    public boolean getFragment() {
        return fragment;
    }

    public void setFragment(boolean fragment) {
        this.fragment = fragment;
    }

    public List<thingML_Stream> getThingml_streams() {
        return thingml_streams;
    }

    public void addThingml_stream(Thingml_stream thingml_stream) {
        this.thingml_streams.add(thingml_stream);
    }
    public thingML_Thing getThingml_thing() {
        return thingml_thing;
    }

    public void setThingml_thing(thingML_Thing thingml_thing) {
        this.thingml_thing = thingml_thing;
    }
    public List<thingML_Port> getThingml_ports() {
        return thingml_ports;
    }

    public void addThingml_port(Thingml_port thingml_port) {
        this.thingml_ports.add(thingml_port);
    }
    public List<thingML_CompositeState> getThingml_compositestates() {
        return thingml_compositestates;
    }

    public void addThingml_compositestate(Thingml_compositestate thingml_compositestate) {
        this.thingml_compositestates.add(thingml_compositestate);
    }
    public List<thingML_Message> getThingml_messages() {
        return thingml_messages;
    }

    public void addThingml_message(Thingml_message thingml_message) {
        this.thingml_messages.add(thingml_message);
    }
    public List<thingML_PropertyAssign> getThingml_propertyassigns() {
        return thingml_propertyassigns;
    }

    public void addThingml_propertyassign(Thingml_propertyassign thingml_propertyassign) {
        this.thingml_propertyassigns.add(thingml_propertyassign);
    }
    public List<thingML_Property> getThingml_propertys() {
        return thingml_propertys;
    }

    public void addThingml_property(Thingml_property thingml_property) {
        this.thingml_propertys.add(thingml_property);
    }
    public List<thingML_Function> getThingml_functions() {
        return thingml_functions;
    }

    public void addThingml_function(Thingml_function thingml_function) {
        this.thingml_functions.add(thingml_function);
    }
    public thingML_Instance getThingml_instance() {
        return thingml_instance;
    }

    public void setThingml_instance(thingML_Instance thingml_instance) {
        this.thingml_instance = thingml_instance;
    }

}
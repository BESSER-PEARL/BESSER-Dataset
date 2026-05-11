





import java.util.List;
import java.util.ArrayList;

public class thingML_ThingMLModel  {






    private List<thingML_Configuration> thingml_configurations;




    private List<thingML_Protocol> thingml_protocols;




    private List<thingML_Type> thingml_types;




    private List<thingML_Import> thingml_imports;


    public thingML_ThingMLModel(
    ) {
        this.thingml_configurations = new ArrayList<>();
        this.thingml_protocols = new ArrayList<>();
        this.thingml_types = new ArrayList<>();
        this.thingml_imports = new ArrayList<>();
    }

    public thingML_ThingMLModel(
        ArrayList<thingML_Configuration> thingml_configurations,        ArrayList<thingML_Protocol> thingml_protocols,        ArrayList<thingML_Type> thingml_types,        ArrayList<thingML_Import> thingml_imports    ) {
        this.thingml_configurations = thingml_configurations;
        this.thingml_protocols = thingml_protocols;
        this.thingml_types = thingml_types;
        this.thingml_imports = thingml_imports;
    }


    public List<thingML_Configuration> getThingml_configurations() {
        return thingml_configurations;
    }

    public void addThingml_configuration(Thingml_configuration thingml_configuration) {
        this.thingml_configurations.add(thingml_configuration);
    }
    public List<thingML_Protocol> getThingml_protocols() {
        return thingml_protocols;
    }

    public void addThingml_protocol(Thingml_protocol thingml_protocol) {
        this.thingml_protocols.add(thingml_protocol);
    }
    public List<thingML_Type> getThingml_types() {
        return thingml_types;
    }

    public void addThingml_type(Thingml_type thingml_type) {
        this.thingml_types.add(thingml_type);
    }
    public List<thingML_Import> getThingml_imports() {
        return thingml_imports;
    }

    public void addThingml_import(Thingml_import thingml_import) {
        this.thingml_imports.add(thingml_import);
    }

}






import java.util.List;
import java.util.ArrayList;

public class thingml_ThingMLModel  {






    private List<thingml_Type> thingml_types;




    private thingml_ThingMLModel thingml_thingmlmodel;




    private List<thingml_Configuration> thingml_configurations;


    public thingml_ThingMLModel(
    ) {
        this.thingml_types = new ArrayList<>();
        this.thingml_configurations = new ArrayList<>();
    }

    public thingml_ThingMLModel(
        ArrayList<thingml_Type> thingml_types,        ArrayList<thingml_Configuration> thingml_configurations    ) {
        this.thingml_types = thingml_types;
        this.thingml_configurations = thingml_configurations;
    }


    public List<thingml_Type> getThingml_types() {
        return thingml_types;
    }

    public void addThingml_type(Thingml_type thingml_type) {
        this.thingml_types.add(thingml_type);
    }
    public thingml_ThingMLModel getThingml_thingmlmodel() {
        return thingml_thingmlmodel;
    }

    public void setThingml_thingmlmodel(thingml_ThingMLModel thingml_thingmlmodel) {
        this.thingml_thingmlmodel = thingml_thingmlmodel;
    }
    public List<thingml_Configuration> getThingml_configurations() {
        return thingml_configurations;
    }

    public void addThingml_configuration(Thingml_configuration thingml_configuration) {
        this.thingml_configurations.add(thingml_configuration);
    }

}
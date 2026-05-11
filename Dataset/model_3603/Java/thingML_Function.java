





import java.util.List;
import java.util.ArrayList;

public class thingML_Function extends AnnotatedElement {

    private String name;





    private List<thingML_Parameter> thingml_parameters;


    public thingML_Function(
        String name    ) {
        super(
        );
        this.name = name;
        this.thingml_parameters = new ArrayList<>();
    }

    public thingML_Function(
        String name        ArrayList<thingML_Parameter> thingml_parameters    ) {
        this.name = name;
        this.thingml_parameters = thingml_parameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<thingML_Parameter> getThingml_parameters() {
        return thingml_parameters;
    }

    public void addThingml_parameter(Thingml_parameter thingml_parameter) {
        this.thingml_parameters.add(thingml_parameter);
    }

}






import java.util.List;
import java.util.ArrayList;

public class org_behavior_LambdaParameter extends KermetaModelElement {

    private String name;





    private behavior_TypeReference behavior_typereference;


    public org_behavior_LambdaParameter(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public behavior_TypeReference getBehavior_typereference() {
        return behavior_typereference;
    }

    public void setBehavior_typereference(behavior_TypeReference behavior_typereference) {
        this.behavior_typereference = behavior_typereference;
    }

}
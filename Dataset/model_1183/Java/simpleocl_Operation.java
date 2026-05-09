





import java.util.List;
import java.util.ArrayList;

public class simpleocl_Operation extends OclFeature {






    private List<simpleocl_Parameter> simpleocl_parameters;




    private simpleocl_Parameter simpleocl_parameter;


    public simpleocl_Operation(
    ) {
        super(
        );
        this.simpleocl_parameters = new ArrayList<>();
    }

    public simpleocl_Operation(
        ArrayList<simpleocl_Parameter> simpleocl_parameters    ) {
        this.simpleocl_parameters = simpleocl_parameters;
    }


    public List<simpleocl_Parameter> getSimpleocl_parameters() {
        return simpleocl_parameters;
    }

    public void addSimpleocl_parameter(Simpleocl_parameter simpleocl_parameter) {
        this.simpleocl_parameters.add(simpleocl_parameter);
    }
    public simpleocl_Parameter getSimpleocl_parameter() {
        return simpleocl_parameter;
    }

    public void setSimpleocl_parameter(simpleocl_Parameter simpleocl_parameter) {
        this.simpleocl_parameter = simpleocl_parameter;
    }

}
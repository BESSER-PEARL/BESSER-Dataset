





import java.util.List;
import java.util.ArrayList;

public class statemachine_GStatemachine extends GCompositeState {

    private String package;





    private List<statemachine_Parameter> statemachine_parameters;


    public statemachine_GStatemachine(
        String package    ) {
        super(
        );
        this.package = package;
        this.statemachine_parameters = new ArrayList<>();
    }

    public statemachine_GStatemachine(
        String package        ArrayList<statemachine_Parameter> statemachine_parameters    ) {
        this.package = package;
        this.statemachine_parameters = statemachine_parameters;
    }

    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }

    public List<statemachine_Parameter> getStatemachine_parameters() {
        return statemachine_parameters;
    }

    public void addStatemachine_parameter(Statemachine_parameter statemachine_parameter) {
        this.statemachine_parameters.add(statemachine_parameter);
    }

}






import java.util.List;
import java.util.ArrayList;

public class UML2_Operation extends MultiplicityElement {






    private List<UML2_Parameter> uml2_parameters;


    public UML2_Operation(
    ) {
        super(
        );
        this.uml2_parameters = new ArrayList<>();
    }

    public UML2_Operation(
        ArrayList<UML2_Parameter> uml2_parameters    ) {
        this.uml2_parameters = uml2_parameters;
    }


    public List<UML2_Parameter> getUml2_parameters() {
        return uml2_parameters;
    }

    public void addUml2_parameter(Uml2_parameter uml2_parameter) {
        this.uml2_parameters.add(uml2_parameter);
    }

}
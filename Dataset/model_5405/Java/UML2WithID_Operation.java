





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Operation extends Element {






    private List<UML2WithID_Parameter> uml2withid_parameters;


    public UML2WithID_Operation(
    ) {
        super(
        );
        this.uml2withid_parameters = new ArrayList<>();
    }

    public UML2WithID_Operation(
        ArrayList<UML2WithID_Parameter> uml2withid_parameters    ) {
        this.uml2withid_parameters = uml2withid_parameters;
    }


    public List<UML2WithID_Parameter> getUml2withid_parameters() {
        return uml2withid_parameters;
    }

    public void addUml2withid_parameter(Uml2withid_parameter uml2withid_parameter) {
        this.uml2withid_parameters.add(uml2withid_parameter);
    }

}
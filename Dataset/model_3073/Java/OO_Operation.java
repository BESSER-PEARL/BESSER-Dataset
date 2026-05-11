





import java.util.List;
import java.util.ArrayList;

public class OO_Operation extends Feature {






    private OO_Parameter oo_parameter;




    private List<OO_Parameter> oo_parameters;


    public OO_Operation(
    ) {
        super(
        );
        this.oo_parameters = new ArrayList<>();
    }

    public OO_Operation(
        ArrayList<OO_Parameter> oo_parameters    ) {
        this.oo_parameters = oo_parameters;
    }


    public OO_Parameter getOo_parameter() {
        return oo_parameter;
    }

    public void setOo_parameter(OO_Parameter oo_parameter) {
        this.oo_parameter = oo_parameter;
    }
    public List<OO_Parameter> getOo_parameters() {
        return oo_parameters;
    }

    public void addOo_parameter(Oo_parameter oo_parameter) {
        this.oo_parameters.add(oo_parameter);
    }

}
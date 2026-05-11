





import java.util.List;
import java.util.ArrayList;

public class eJSL_Template extends Extension {






    private List<eJSL_Parameter> ejsl_parameters;


    public eJSL_Template(
    ) {
        super(
        );
        this.ejsl_parameters = new ArrayList<>();
    }

    public eJSL_Template(
        ArrayList<eJSL_Parameter> ejsl_parameters    ) {
        this.ejsl_parameters = ejsl_parameters;
    }


    public List<eJSL_Parameter> getEjsl_parameters() {
        return ejsl_parameters;
    }

    public void addEjsl_parameter(Ejsl_parameter ejsl_parameter) {
        this.ejsl_parameters.add(ejsl_parameter);
    }

}
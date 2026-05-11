





import java.util.List;
import java.util.ArrayList;

public class eJSL_ParameterGroup  {

    private String name;
    private String label;





    private List<eJSL_Parameter> ejsl_parameters;




    private List<eJSL_Parameter> ejsl_parameters;




    private eJSL_EJSLPart ejsl_ejslpart;


    public eJSL_ParameterGroup(
        String name,        String label    ) {
        this.name = name;
        this.label = label;
        this.ejsl_parameters = new ArrayList<>();
        this.ejsl_parameters = new ArrayList<>();
    }

    public eJSL_ParameterGroup(
        String name,        String label        ArrayList<eJSL_Parameter> ejsl_parameters,        ArrayList<eJSL_Parameter> ejsl_parameters    ) {
        this.name = name;
        this.label = label;
        this.ejsl_parameters = ejsl_parameters;
        this.ejsl_parameters = ejsl_parameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<eJSL_Parameter> getEjsl_parameters() {
        return ejsl_parameters;
    }

    public void addEjsl_parameter(Ejsl_parameter ejsl_parameter) {
        this.ejsl_parameters.add(ejsl_parameter);
    }
    public List<eJSL_Parameter> getEjsl_parameters() {
        return ejsl_parameters;
    }

    public void addEjsl_parameter(Ejsl_parameter ejsl_parameter) {
        this.ejsl_parameters.add(ejsl_parameter);
    }
    public eJSL_EJSLPart getEjsl_ejslpart() {
        return ejsl_ejslpart;
    }

    public void setEjsl_ejslpart(eJSL_EJSLPart ejsl_ejslpart) {
        this.ejsl_ejslpart = ejsl_ejslpart;
    }

}
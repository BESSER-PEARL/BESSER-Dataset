





import java.util.List;
import java.util.ArrayList;

public class eJSL_Page  {

    private String name;





    private List<eJSL_Parameter> ejsl_parameters;




    private List<eJSL_Parameter> ejsl_parameters;




    private List<eJSL_PageAction> ejsl_pageactions;




    private eJSL_Feature ejsl_feature;




    private List<eJSL_ParameterGroup> ejsl_parametergroups;


    public eJSL_Page(
        String name    ) {
        this.name = name;
        this.ejsl_parameters = new ArrayList<>();
        this.ejsl_parameters = new ArrayList<>();
        this.ejsl_pageactions = new ArrayList<>();
        this.ejsl_parametergroups = new ArrayList<>();
    }

    public eJSL_Page(
        String name        ArrayList<eJSL_Parameter> ejsl_parameters,        ArrayList<eJSL_Parameter> ejsl_parameters,        ArrayList<eJSL_PageAction> ejsl_pageactions,        ArrayList<eJSL_ParameterGroup> ejsl_parametergroups    ) {
        this.name = name;
        this.ejsl_parameters = ejsl_parameters;
        this.ejsl_parameters = ejsl_parameters;
        this.ejsl_pageactions = ejsl_pageactions;
        this.ejsl_parametergroups = ejsl_parametergroups;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public List<eJSL_PageAction> getEjsl_pageactions() {
        return ejsl_pageactions;
    }

    public void addEjsl_pageaction(Ejsl_pageaction ejsl_pageaction) {
        this.ejsl_pageactions.add(ejsl_pageaction);
    }
    public eJSL_Feature getEjsl_feature() {
        return ejsl_feature;
    }

    public void setEjsl_feature(eJSL_Feature ejsl_feature) {
        this.ejsl_feature = ejsl_feature;
    }
    public List<eJSL_ParameterGroup> getEjsl_parametergroups() {
        return ejsl_parametergroups;
    }

    public void addEjsl_parametergroup(Ejsl_parametergroup ejsl_parametergroup) {
        this.ejsl_parametergroups.add(ejsl_parametergroup);
    }

}






import java.util.List;
import java.util.ArrayList;

public class applauseDsl_DataSourceAccessMethod  {

    private String name;
    private boolean returnsMany;





    private applauseDsl_RESTSpecification applausedsl_restspecification;




    private applauseDsl_RESTMethodCall applausedsl_restmethodcall;




    private List<applauseDsl_Parameter> applausedsl_parameters;




    private applauseDsl_DataSource applausedsl_datasource;


    public applauseDsl_DataSourceAccessMethod(
        String name,        boolean returnsMany    ) {
        this.name = name;
        this.returnsMany = returnsMany;
        this.applausedsl_parameters = new ArrayList<>();
    }

    public applauseDsl_DataSourceAccessMethod(
        String name,        boolean returnsMany        ArrayList<applauseDsl_Parameter> applausedsl_parameters    ) {
        this.name = name;
        this.returnsMany = returnsMany;
        this.applausedsl_parameters = applausedsl_parameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getReturnsmany() {
        return returnsMany;
    }

    public void setReturnsmany(boolean returnsMany) {
        this.returnsMany = returnsMany;
    }

    public applauseDsl_RESTSpecification getApplausedsl_restspecification() {
        return applausedsl_restspecification;
    }

    public void setApplausedsl_restspecification(applauseDsl_RESTSpecification applausedsl_restspecification) {
        this.applausedsl_restspecification = applausedsl_restspecification;
    }
    public applauseDsl_RESTMethodCall getApplausedsl_restmethodcall() {
        return applausedsl_restmethodcall;
    }

    public void setApplausedsl_restmethodcall(applauseDsl_RESTMethodCall applausedsl_restmethodcall) {
        this.applausedsl_restmethodcall = applausedsl_restmethodcall;
    }
    public List<applauseDsl_Parameter> getApplausedsl_parameters() {
        return applausedsl_parameters;
    }

    public void addApplausedsl_parameter(Applausedsl_parameter applausedsl_parameter) {
        this.applausedsl_parameters.add(applausedsl_parameter);
    }
    public applauseDsl_DataSource getApplausedsl_datasource() {
        return applausedsl_datasource;
    }

    public void setApplausedsl_datasource(applauseDsl_DataSource applausedsl_datasource) {
        this.applausedsl_datasource = applausedsl_datasource;
    }

}
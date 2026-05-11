





import java.util.List;
import java.util.ArrayList;

public class eJSL_Plugin extends Extension {

    private String type;





    private List<eJSL_Parameter> ejsl_parameters;




    private List<eJSL_Entity> ejsl_entitys;


    public eJSL_Plugin(
        String type    ) {
        super(
        );
        this.type = type;
        this.ejsl_parameters = new ArrayList<>();
        this.ejsl_entitys = new ArrayList<>();
    }

    public eJSL_Plugin(
        String type        ArrayList<eJSL_Parameter> ejsl_parameters,        ArrayList<eJSL_Entity> ejsl_entitys    ) {
        this.type = type;
        this.ejsl_parameters = ejsl_parameters;
        this.ejsl_entitys = ejsl_entitys;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<eJSL_Parameter> getEjsl_parameters() {
        return ejsl_parameters;
    }

    public void addEjsl_parameter(Ejsl_parameter ejsl_parameter) {
        this.ejsl_parameters.add(ejsl_parameter);
    }
    public List<eJSL_Entity> getEjsl_entitys() {
        return ejsl_entitys;
    }

    public void addEjsl_entity(Ejsl_entity ejsl_entity) {
        this.ejsl_entitys.add(ejsl_entity);
    }

}
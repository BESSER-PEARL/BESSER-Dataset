





import java.util.List;
import java.util.ArrayList;

public class rapidml_Method extends Extensible, RESTElement, HasSecurityValue {

    private String id;
    private String httpMethod;





    private rapidml_ResourceDefinition rapidml_resourcedefinition;




    private rapidml_ResourceDefinition rapidml_resourcedefinition;


    public rapidml_Method(
        String id,        String httpMethod    ) {
        super(
        );
        this.id = id;
        this.httpMethod = httpMethod;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getHttpmethod() {
        return httpMethod;
    }

    public void setHttpmethod(String httpMethod) {
        this.httpMethod = httpMethod;
    }

    public rapidml_ResourceDefinition getRapidml_resourcedefinition() {
        return rapidml_resourcedefinition;
    }

    public void setRapidml_resourcedefinition(rapidml_ResourceDefinition rapidml_resourcedefinition) {
        this.rapidml_resourcedefinition = rapidml_resourcedefinition;
    }
    public rapidml_ResourceDefinition getRapidml_resourcedefinition() {
        return rapidml_resourcedefinition;
    }

    public void setRapidml_resourcedefinition(rapidml_ResourceDefinition rapidml_resourcedefinition) {
        this.rapidml_resourcedefinition = rapidml_resourcedefinition;
    }

}
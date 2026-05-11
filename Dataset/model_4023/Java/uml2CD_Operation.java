





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Operation extends NamedElement {

    private String visibility;
    private String body;
    private String isQuery;





    private List<uml2CD_Parameter> uml2cd_parameters;




    private uml2CD_Operation uml2cd_operation;


    public uml2CD_Operation(
        String visibility,        String body,        String isQuery    ) {
        super(
        );
        this.visibility = visibility;
        this.body = body;
        this.isQuery = isQuery;
        this.uml2cd_parameters = new ArrayList<>();
    }

    public uml2CD_Operation(
        String visibility,        String body,        String isQuery        ArrayList<uml2CD_Parameter> uml2cd_parameters    ) {
        this.visibility = visibility;
        this.body = body;
        this.isQuery = isQuery;
        this.uml2cd_parameters = uml2cd_parameters;
    }

    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getIsquery() {
        return isQuery;
    }

    public void setIsquery(String isQuery) {
        this.isQuery = isQuery;
    }

    public List<uml2CD_Parameter> getUml2cd_parameters() {
        return uml2cd_parameters;
    }

    public void addUml2cd_parameter(Uml2cd_parameter uml2cd_parameter) {
        this.uml2cd_parameters.add(uml2cd_parameter);
    }
    public uml2CD_Operation getUml2cd_operation() {
        return uml2cd_operation;
    }

    public void setUml2cd_operation(uml2CD_Operation uml2cd_operation) {
        this.uml2cd_operation = uml2cd_operation;
    }

}
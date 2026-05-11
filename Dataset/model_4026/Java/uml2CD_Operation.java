





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Operation extends NamedElement {

    private String body;
    private String visibility;
    private String isQuery;





    private List<uml2CD_Operation> uml2cd_operations;




    private uml2CD_Class uml2cd_class;


    public uml2CD_Operation(
        String body,        String visibility,        String isQuery    ) {
        super(
        );
        this.body = body;
        this.visibility = visibility;
        this.isQuery = isQuery;
        this.uml2cd_operations = new ArrayList<>();
    }

    public uml2CD_Operation(
        String body,        String visibility,        String isQuery        ArrayList<uml2CD_Operation> uml2cd_operations    ) {
        this.body = body;
        this.visibility = visibility;
        this.isQuery = isQuery;
        this.uml2cd_operations = uml2cd_operations;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getIsquery() {
        return isQuery;
    }

    public void setIsquery(String isQuery) {
        this.isQuery = isQuery;
    }

    public List<uml2CD_Operation> getUml2cd_operations() {
        return uml2cd_operations;
    }

    public void addUml2cd_operation(Uml2cd_operation uml2cd_operation) {
        this.uml2cd_operations.add(uml2cd_operation);
    }
    public uml2CD_Class getUml2cd_class() {
        return uml2cd_class;
    }

    public void setUml2cd_class(uml2CD_Class uml2cd_class) {
        this.uml2cd_class = uml2cd_class;
    }

}






import java.util.List;
import java.util.ArrayList;

public class uml2CD_Operation extends NamedElement {

    private String body;
    private String isQuery;
    private String visibility;





    private List<uml2CD_Operation> uml2cd_operations;


    public uml2CD_Operation(
        String body,        String isQuery,        String visibility    ) {
        super(
        );
        this.body = body;
        this.isQuery = isQuery;
        this.visibility = visibility;
        this.uml2cd_operations = new ArrayList<>();
    }

    public uml2CD_Operation(
        String body,        String isQuery,        String visibility        ArrayList<uml2CD_Operation> uml2cd_operations    ) {
        this.body = body;
        this.isQuery = isQuery;
        this.visibility = visibility;
        this.uml2cd_operations = uml2cd_operations;
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
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public List<uml2CD_Operation> getUml2cd_operations() {
        return uml2cd_operations;
    }

    public void addUml2cd_operation(Uml2cd_operation uml2cd_operation) {
        this.uml2cd_operations.add(uml2cd_operation);
    }

}






import java.util.List;
import java.util.ArrayList;

public class uml2CD_Operation extends NamedElement {

    private String visibility;
    private String isQuery;
    private String body;





    private uml2CD_Operation uml2cd_operation;


    public uml2CD_Operation(
        String visibility,        String isQuery,        String body    ) {
        super(
        );
        this.visibility = visibility;
        this.isQuery = isQuery;
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
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public uml2CD_Operation getUml2cd_operation() {
        return uml2cd_operation;
    }

    public void setUml2cd_operation(uml2CD_Operation uml2cd_operation) {
        this.uml2cd_operation = uml2cd_operation;
    }

}
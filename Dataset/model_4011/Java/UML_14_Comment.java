





import java.util.List;
import java.util.ArrayList;

public class UML_14_Comment  {

    private String body;





    private UML_14_NamedElement uml_14_namedelement;


    public UML_14_Comment(
        String body    ) {
        this.body = body;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public UML_14_NamedElement getUml_14_namedelement() {
        return uml_14_namedelement;
    }

    public void setUml_14_namedelement(UML_14_NamedElement uml_14_namedelement) {
        this.uml_14_namedelement = uml_14_namedelement;
    }

}
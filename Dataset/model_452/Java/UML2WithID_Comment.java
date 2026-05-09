





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Comment extends TemplateableElement {

    private String body;





    private UML2WithID_StringExpression uml2withid_stringexpression;


    public UML2WithID_Comment(
        String body    ) {
        super(
        );
        this.body = body;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public UML2WithID_StringExpression getUml2withid_stringexpression() {
        return uml2withid_stringexpression;
    }

    public void setUml2withid_stringexpression(UML2WithID_StringExpression uml2withid_stringexpression) {
        this.uml2withid_stringexpression = uml2withid_stringexpression;
    }

}






import java.util.List;
import java.util.ArrayList;

public class XHTML_Form extends FieldsetElement, ObjectElement, MapElementContent, Attrs, Block {

    private String method;





    private URI uri;




    private ScriptExpression scriptexpression;




    private ContentType contenttype;




    private ScriptExpression scriptexpression;


    public XHTML_Form(
        String method    ) {
        super(
        );
        this.method = method;
    }


    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }

    public URI getUri() {
        return uri;
    }

    public void setUri(URI uri) {
        this.uri = uri;
    }
    public ScriptExpression getScriptexpression() {
        return scriptexpression;
    }

    public void setScriptexpression(ScriptExpression scriptexpression) {
        this.scriptexpression = scriptexpression;
    }
    public ContentType getContenttype() {
        return contenttype;
    }

    public void setContenttype(ContentType contenttype) {
        this.contenttype = contenttype;
    }
    public ScriptExpression getScriptexpression() {
        return scriptexpression;
    }

    public void setScriptexpression(ScriptExpression scriptexpression) {
        this.scriptexpression = scriptexpression;
    }

}
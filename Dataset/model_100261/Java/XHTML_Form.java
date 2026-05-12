





import java.util.List;
import java.util.ArrayList;

public class XHTML_Form extends MapElementContent, FieldsetElement, ObjectElement, Block, Attrs {

    private String method;



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


}
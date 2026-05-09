





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Comment extends Element {

    private String annotatedElement;
    private String body;



    public UMLModel_Comment(
        String annotatedElement,        String body    ) {
        super(
        );
        this.annotatedElement = annotatedElement;
        this.body = body;
    }


    public String getAnnotatedelement() {
        return annotatedElement;
    }

    public void setAnnotatedelement(String annotatedElement) {
        this.annotatedElement = annotatedElement;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }


}
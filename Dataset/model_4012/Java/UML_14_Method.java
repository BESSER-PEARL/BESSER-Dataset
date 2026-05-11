





import java.util.List;
import java.util.ArrayList;

public class UML_14_Method extends NamedElement {

    private String body;
    private String visibility;



    public UML_14_Method(
        String body,        String visibility    ) {
        super(
        );
        this.body = body;
        this.visibility = visibility;
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


}
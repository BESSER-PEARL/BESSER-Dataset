





import java.util.List;
import java.util.ArrayList;

public class documentation_XML extends Fragment, NamedElement {

    private String contextClassName;
    private String resource;



    public documentation_XML(
        String contextClassName,        String resource    ) {
        super(
        );
        this.contextClassName = contextClassName;
        this.resource = resource;
    }


    public String getContextclassname() {
        return contextClassName;
    }

    public void setContextclassname(String contextClassName) {
        this.contextClassName = contextClassName;
    }
    public String getResource() {
        return resource;
    }

    public void setResource(String resource) {
        this.resource = resource;
    }


}
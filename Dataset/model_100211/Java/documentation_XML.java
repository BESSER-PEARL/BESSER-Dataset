





import java.util.List;
import java.util.ArrayList;

public class documentation_XML extends NamedElement, Fragment {

    private String contextClassName;
    private String resource;
    private String content;



    public documentation_XML(
        String contextClassName,        String resource,        String content    ) {
        super(
        );
        this.contextClassName = contextClassName;
        this.resource = resource;
        this.content = content;
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
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


}
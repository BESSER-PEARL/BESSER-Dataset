





import java.util.List;
import java.util.ArrayList;

public class documentation_Image extends NamedElement, Fragment {

    private String originalSource;
    private String resource;
    private String contextClassName;



    public documentation_Image(
        String originalSource,        String resource,        String contextClassName    ) {
        super(
        );
        this.originalSource = originalSource;
        this.resource = resource;
        this.contextClassName = contextClassName;
    }


    public String getOriginalsource() {
        return originalSource;
    }

    public void setOriginalsource(String originalSource) {
        this.originalSource = originalSource;
    }
    public String getResource() {
        return resource;
    }

    public void setResource(String resource) {
        this.resource = resource;
    }
    public String getContextclassname() {
        return contextClassName;
    }

    public void setContextclassname(String contextClassName) {
        this.contextClassName = contextClassName;
    }


}
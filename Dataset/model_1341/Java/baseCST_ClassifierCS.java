





import java.util.List;
import java.util.ArrayList;

public class baseCST_ClassifierCS extends TypeCS, NamedElementCS, TemplateableElementCS {

    private String qualifier;
    private String instanceClassName;



    public baseCST_ClassifierCS(
        String qualifier,        String instanceClassName    ) {
        super(
        );
        this.qualifier = qualifier;
        this.instanceClassName = instanceClassName;
    }


    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }
    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }


}
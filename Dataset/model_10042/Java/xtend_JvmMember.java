





import java.util.List;
import java.util.ArrayList;

public class xtend_JvmMember extends JvmIdentifiableElement, JvmAnnotationTarget {

    private String simpleName;
    private String identifier;
    private String visibility;



    public xtend_JvmMember(
        String simpleName,        String identifier,        String visibility    ) {
        super(
        );
        this.simpleName = simpleName;
        this.identifier = identifier;
        this.visibility = visibility;
    }


    public String getSimplename() {
        return simpleName;
    }

    public void setSimplename(String simpleName) {
        this.simpleName = simpleName;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}
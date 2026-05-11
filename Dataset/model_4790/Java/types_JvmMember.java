





import java.util.List;
import java.util.ArrayList;

public class types_JvmMember extends JvmAnnotationTarget, JvmIdentifiableElement {

    private String simpleName;
    private String visibility;
    private String identifier;



    public types_JvmMember(
        String simpleName,        String visibility,        String identifier    ) {
        super(
        );
        this.simpleName = simpleName;
        this.visibility = visibility;
        this.identifier = identifier;
    }


    public String getSimplename() {
        return simpleName;
    }

    public void setSimplename(String simpleName) {
        this.simpleName = simpleName;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}
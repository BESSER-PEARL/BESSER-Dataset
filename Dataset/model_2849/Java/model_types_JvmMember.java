





import java.util.List;
import java.util.ArrayList;

public class model_types_JvmMember extends JvmAnnotationTarget {

    private String modifiers;
    private String simpleName;
    private String visibility;
    private String identifier;





    private JvmDeclaredType jvmdeclaredtype;


    public model_types_JvmMember(
        String modifiers,        String simpleName,        String visibility,        String identifier    ) {
        super(
        );
        this.modifiers = modifiers;
        this.simpleName = simpleName;
        this.visibility = visibility;
        this.identifier = identifier;
    }


    public String getModifiers() {
        return modifiers;
    }

    public void setModifiers(String modifiers) {
        this.modifiers = modifiers;
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

    public JvmDeclaredType getJvmdeclaredtype() {
        return jvmdeclaredtype;
    }

    public void setJvmdeclaredtype(JvmDeclaredType jvmdeclaredtype) {
        this.jvmdeclaredtype = jvmdeclaredtype;
    }

}
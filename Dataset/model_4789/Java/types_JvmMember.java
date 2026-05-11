





import java.util.List;
import java.util.ArrayList;

public class types_JvmMember extends JvmAnnotationTarget {

    private String visibility;
    private boolean deprecated;
    private String identifier;
    private String simpleName;





    private types_JvmDeclaredType types_jvmdeclaredtype;




    private types_JvmDeclaredType types_jvmdeclaredtype;


    public types_JvmMember(
        String visibility,        boolean deprecated,        String identifier,        String simpleName    ) {
        super(
        );
        this.visibility = visibility;
        this.deprecated = deprecated;
        this.identifier = identifier;
        this.simpleName = simpleName;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getDeprecated() {
        return deprecated;
    }

    public void setDeprecated(boolean deprecated) {
        this.deprecated = deprecated;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getSimplename() {
        return simpleName;
    }

    public void setSimplename(String simpleName) {
        this.simpleName = simpleName;
    }

    public types_JvmDeclaredType getTypes_jvmdeclaredtype() {
        return types_jvmdeclaredtype;
    }

    public void setTypes_jvmdeclaredtype(types_JvmDeclaredType types_jvmdeclaredtype) {
        this.types_jvmdeclaredtype = types_jvmdeclaredtype;
    }
    public types_JvmDeclaredType getTypes_jvmdeclaredtype() {
        return types_jvmdeclaredtype;
    }

    public void setTypes_jvmdeclaredtype(types_JvmDeclaredType types_jvmdeclaredtype) {
        this.types_jvmdeclaredtype = types_jvmdeclaredtype;
    }

}
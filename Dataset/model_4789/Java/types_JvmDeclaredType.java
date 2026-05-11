





import java.util.List;
import java.util.ArrayList;

public class types_JvmDeclaredType extends JvmMember, JvmComponentType {

    private String packageName;
    private boolean final;
    private boolean static;
    private boolean abstract;



    public types_JvmDeclaredType(
        String packageName,        boolean final,        boolean static,        boolean abstract    ) {
        super(
        );
        this.packageName = packageName;
        this.final = final;
        this.static = static;
        this.abstract = abstract;
    }


    public String getPackagename() {
        return packageName;
    }

    public void setPackagename(String packageName) {
        this.packageName = packageName;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }


}
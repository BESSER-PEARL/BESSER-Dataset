





import java.util.List;
import java.util.ArrayList;

public class types_JvmDeclaredType extends JvmComponentType, JvmMember {

    private boolean abstract;
    private boolean final;
    private String packageName;
    private boolean static;



    public types_JvmDeclaredType(
        boolean abstract,        boolean final,        String packageName,        boolean static    ) {
        super(
        );
        this.abstract = abstract;
        this.final = final;
        this.packageName = packageName;
        this.static = static;
    }


    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public String getPackagename() {
        return packageName;
    }

    public void setPackagename(String packageName) {
        this.packageName = packageName;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }


}
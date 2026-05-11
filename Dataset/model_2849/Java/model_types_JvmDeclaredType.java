





import java.util.List;
import java.util.ArrayList;

public class model_types_JvmDeclaredType extends types_JvmMember, types_JvmComponentType {

    private String packageName;
    private boolean abstract;
    private boolean final;
    private boolean exported;
    private boolean static;



    public model_types_JvmDeclaredType(
        String packageName,        boolean abstract,        boolean final,        boolean exported,        boolean static    ) {
        super(
        );
        this.packageName = packageName;
        this.abstract = abstract;
        this.final = final;
        this.exported = exported;
        this.static = static;
    }


    public String getPackagename() {
        return packageName;
    }

    public void setPackagename(String packageName) {
        this.packageName = packageName;
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
    public boolean getExported() {
        return exported;
    }

    public void setExported(boolean exported) {
        this.exported = exported;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }


}
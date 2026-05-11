





import java.util.List;
import java.util.ArrayList;

public class types_JvmOperation extends JvmExecutable {

    private boolean abstract;
    private boolean final;
    private boolean static;





    private types_JvmTypeReference types_jvmtypereference;


    public types_JvmOperation(
        boolean abstract,        boolean final,        boolean static    ) {
        super(
        );
        this.abstract = abstract;
        this.final = final;
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
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public types_JvmTypeReference getTypes_jvmtypereference() {
        return types_jvmtypereference;
    }

    public void setTypes_jvmtypereference(types_JvmTypeReference types_jvmtypereference) {
        this.types_jvmtypereference = types_jvmtypereference;
    }

}
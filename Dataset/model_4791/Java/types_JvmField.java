





import java.util.List;
import java.util.ArrayList;

public class types_JvmField extends JvmFeature {

    private boolean static;
    private boolean final;





    private types_JvmTypeReference types_jvmtypereference;


    public types_JvmField(
        boolean static,        boolean final    ) {
        super(
        );
        this.static = static;
        this.final = final;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }

    public types_JvmTypeReference getTypes_jvmtypereference() {
        return types_jvmtypereference;
    }

    public void setTypes_jvmtypereference(types_JvmTypeReference types_jvmtypereference) {
        this.types_jvmtypereference = types_jvmtypereference;
    }

}






import java.util.List;
import java.util.ArrayList;

public class model_types_JvmField extends JvmFeature {

    private boolean volatile;
    private boolean transient;
    private boolean static;
    private boolean final;



    public model_types_JvmField(
        boolean volatile,        boolean transient,        boolean static,        boolean final    ) {
        super(
        );
        this.volatile = volatile;
        this.transient = transient;
        this.static = static;
        this.final = final;
    }


    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
    }
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
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


}
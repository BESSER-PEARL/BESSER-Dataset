





import java.util.List;
import java.util.ArrayList;

public class types_JvmField extends JvmFeature {

    private boolean final;
    private boolean constant;
    private boolean transient;
    private String constantValue;
    private boolean static;
    private boolean volatile;



    public types_JvmField(
        boolean final,        boolean constant,        boolean transient,        String constantValue,        boolean static,        boolean volatile    ) {
        super(
        );
        this.final = final;
        this.constant = constant;
        this.transient = transient;
        this.constantValue = constantValue;
        this.static = static;
        this.volatile = volatile;
    }


    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public String getConstantvalue() {
        return constantValue;
    }

    public void setConstantvalue(String constantValue) {
        this.constantValue = constantValue;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
    }


}
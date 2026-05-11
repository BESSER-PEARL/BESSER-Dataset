





import java.util.List;
import java.util.ArrayList;

public class model_types_JvmOperation extends JvmExecutable {

    private boolean final;
    private boolean synchronized;
    private boolean default;
    private boolean static;
    private boolean abstract;
    private boolean strictFloatingPoint;
    private boolean native;





    private XExpression xexpression;




    private XExpression xexpression;


    public model_types_JvmOperation(
        boolean final,        boolean synchronized,        boolean default,        boolean static,        boolean abstract,        boolean strictFloatingPoint,        boolean native    ) {
        super(
        );
        this.final = final;
        this.synchronized = synchronized;
        this.default = default;
        this.static = static;
        this.abstract = abstract;
        this.strictFloatingPoint = strictFloatingPoint;
        this.native = native;
    }


    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }
    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
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
    public boolean getStrictfloatingpoint() {
        return strictFloatingPoint;
    }

    public void setStrictfloatingpoint(boolean strictFloatingPoint) {
        this.strictFloatingPoint = strictFloatingPoint;
    }
    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
        this.native = native;
    }

    public XExpression getXexpression() {
        return xexpression;
    }

    public void setXexpression(XExpression xexpression) {
        this.xexpression = xexpression;
    }
    public XExpression getXexpression() {
        return xexpression;
    }

    public void setXexpression(XExpression xexpression) {
        this.xexpression = xexpression;
    }

}
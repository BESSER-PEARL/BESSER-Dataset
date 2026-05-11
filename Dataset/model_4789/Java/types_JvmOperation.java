





import java.util.List;
import java.util.ArrayList;

public class types_JvmOperation extends JvmExecutable {

    private boolean native;
    private boolean synchronized;
    private boolean final;
    private boolean static;
    private boolean abstract;
    private boolean strictFloatingPoint;
    private boolean default;



    public types_JvmOperation(
        boolean native,        boolean synchronized,        boolean final,        boolean static,        boolean abstract,        boolean strictFloatingPoint,        boolean default    ) {
        super(
        );
        this.native = native;
        this.synchronized = synchronized;
        this.final = final;
        this.static = static;
        this.abstract = abstract;
        this.strictFloatingPoint = strictFloatingPoint;
        this.default = default;
    }


    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
        this.native = native;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
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
    public boolean getStrictfloatingpoint() {
        return strictFloatingPoint;
    }

    public void setStrictfloatingpoint(boolean strictFloatingPoint) {
        this.strictFloatingPoint = strictFloatingPoint;
    }
    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }


}
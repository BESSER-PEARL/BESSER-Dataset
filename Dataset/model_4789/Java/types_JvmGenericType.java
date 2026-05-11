





import java.util.List;
import java.util.ArrayList;

public class types_JvmGenericType extends JvmTypeParameterDeclarator, JvmDeclaredType {

    private boolean interface;
    private boolean anonymous;
    private boolean strictFloatingPoint;



    public types_JvmGenericType(
        boolean interface,        boolean anonymous,        boolean strictFloatingPoint    ) {
        super(
        );
        this.interface = interface;
        this.anonymous = anonymous;
        this.strictFloatingPoint = strictFloatingPoint;
    }


    public boolean getInterface() {
        return interface;
    }

    public void setInterface(boolean interface) {
        this.interface = interface;
    }
    public boolean getAnonymous() {
        return anonymous;
    }

    public void setAnonymous(boolean anonymous) {
        this.anonymous = anonymous;
    }
    public boolean getStrictfloatingpoint() {
        return strictFloatingPoint;
    }

    public void setStrictfloatingpoint(boolean strictFloatingPoint) {
        this.strictFloatingPoint = strictFloatingPoint;
    }


}
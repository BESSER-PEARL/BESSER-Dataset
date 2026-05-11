





import java.util.List;
import java.util.ArrayList;

public class model_types_JvmGenericType extends types_JvmTypeParameterDeclarator, types_JvmDeclaredType {

    private boolean interface;
    private boolean strictFloatingPoint;



    public model_types_JvmGenericType(
        boolean interface,        boolean strictFloatingPoint    ) {
        super(
        );
        this.interface = interface;
        this.strictFloatingPoint = strictFloatingPoint;
    }


    public boolean getInterface() {
        return interface;
    }

    public void setInterface(boolean interface) {
        this.interface = interface;
    }
    public boolean getStrictfloatingpoint() {
        return strictFloatingPoint;
    }

    public void setStrictfloatingpoint(boolean strictFloatingPoint) {
        this.strictFloatingPoint = strictFloatingPoint;
    }


}
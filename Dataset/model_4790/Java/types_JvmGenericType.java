





import java.util.List;
import java.util.ArrayList;

public class types_JvmGenericType extends JvmDeclaredType, JvmTypeParameterDeclarator {

    private boolean interface;



    public types_JvmGenericType(
        boolean interface    ) {
        super(
        );
        this.interface = interface;
    }


    public boolean getInterface() {
        return interface;
    }

    public void setInterface(boolean interface) {
        this.interface = interface;
    }


}
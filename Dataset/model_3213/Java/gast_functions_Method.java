





import java.util.List;
import java.util.ArrayList;

public class gast_functions_Method extends functions_Function, types_Member {

    private boolean propertyMethod;





    private GASTClass gastclass;


    public gast_functions_Method(
        boolean propertyMethod    ) {
        super(
        );
        this.propertyMethod = propertyMethod;
    }


    public boolean getPropertymethod() {
        return propertyMethod;
    }

    public void setPropertymethod(boolean propertyMethod) {
        this.propertyMethod = propertyMethod;
    }

    public GASTClass getGastclass() {
        return gastclass;
    }

    public void setGastclass(GASTClass gastclass) {
        this.gastclass = gastclass;
    }

}






import java.util.List;
import java.util.ArrayList;

public class gast_variables_Field extends types_Member, variables_Variable {

    private boolean propertyField;





    private GASTClass gastclass;


    public gast_variables_Field(
        boolean propertyField    ) {
        super(
        );
        this.propertyField = propertyField;
    }


    public boolean getPropertyfield() {
        return propertyField;
    }

    public void setPropertyfield(boolean propertyField) {
        this.propertyField = propertyField;
    }

    public GASTClass getGastclass() {
        return gastclass;
    }

    public void setGastclass(GASTClass gastclass) {
        this.gastclass = gastclass;
    }

}
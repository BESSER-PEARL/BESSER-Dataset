





import java.util.List;
import java.util.ArrayList;

public class gast_variables_Field extends variables_Variable, types_Member {

    private boolean propertyField;



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


}
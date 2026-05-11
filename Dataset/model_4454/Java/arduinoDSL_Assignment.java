





import java.util.List;
import java.util.ArrayList;

public class arduinoDSL_Assignment extends SimpleStatement {






    private arduinoDSL_EObject arduinodsl_eobject;




    private arduinoDSL_Attribute arduinodsl_attribute;


    public arduinoDSL_Assignment(
    ) {
        super(
        );
    }



    public arduinoDSL_EObject getArduinodsl_eobject() {
        return arduinodsl_eobject;
    }

    public void setArduinodsl_eobject(arduinoDSL_EObject arduinodsl_eobject) {
        this.arduinodsl_eobject = arduinodsl_eobject;
    }
    public arduinoDSL_Attribute getArduinodsl_attribute() {
        return arduinodsl_attribute;
    }

    public void setArduinodsl_attribute(arduinoDSL_Attribute arduinodsl_attribute) {
        this.arduinodsl_attribute = arduinodsl_attribute;
    }

}






import java.util.List;
import java.util.ArrayList;

public class arduinoDSL_Rate  {

    private int value;





    private arduinoDSL_ComponentBody arduinodsl_componentbody;


    public arduinoDSL_Rate(
        int value    ) {
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public arduinoDSL_ComponentBody getArduinodsl_componentbody() {
        return arduinodsl_componentbody;
    }

    public void setArduinodsl_componentbody(arduinoDSL_ComponentBody arduinodsl_componentbody) {
        this.arduinodsl_componentbody = arduinodsl_componentbody;
    }

}
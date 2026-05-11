





import java.util.List;
import java.util.ArrayList;

public class arduinoDSL_Smoothing  {

    private float value;





    private arduinoDSL_ComponentBody arduinodsl_componentbody;


    public arduinoDSL_Smoothing(
        float value    ) {
        this.value = value;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }

    public arduinoDSL_ComponentBody getArduinodsl_componentbody() {
        return arduinodsl_componentbody;
    }

    public void setArduinodsl_componentbody(arduinoDSL_ComponentBody arduinodsl_componentbody) {
        this.arduinodsl_componentbody = arduinodsl_componentbody;
    }

}
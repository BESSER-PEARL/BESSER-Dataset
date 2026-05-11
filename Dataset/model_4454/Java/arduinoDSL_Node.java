





import java.util.List;
import java.util.ArrayList;

public class arduinoDSL_Node  {

    private String name;





    private arduinoDSL_Attribute arduinodsl_attribute;


    public arduinoDSL_Node(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public arduinoDSL_Attribute getArduinodsl_attribute() {
        return arduinodsl_attribute;
    }

    public void setArduinodsl_attribute(arduinoDSL_Attribute arduinodsl_attribute) {
        this.arduinodsl_attribute = arduinodsl_attribute;
    }

}
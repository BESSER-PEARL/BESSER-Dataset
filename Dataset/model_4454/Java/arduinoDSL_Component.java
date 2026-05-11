





import java.util.List;
import java.util.ArrayList;

public class arduinoDSL_Component  {

    private String name;





    private arduinoDSL_Node arduinodsl_node;




    private arduinoDSL_Attribute arduinodsl_attribute;


    public arduinoDSL_Component(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public arduinoDSL_Node getArduinodsl_node() {
        return arduinodsl_node;
    }

    public void setArduinodsl_node(arduinoDSL_Node arduinodsl_node) {
        this.arduinodsl_node = arduinodsl_node;
    }
    public arduinoDSL_Attribute getArduinodsl_attribute() {
        return arduinodsl_attribute;
    }

    public void setArduinodsl_attribute(arduinoDSL_Attribute arduinodsl_attribute) {
        this.arduinodsl_attribute = arduinodsl_attribute;
    }

}
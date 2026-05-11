





import java.util.List;
import java.util.ArrayList;

public class arduinoDSL_Board  {

    private String b;





    private arduinoDSL_NodeDefinition arduinodsl_nodedefinition;


    public arduinoDSL_Board(
        String b    ) {
        this.b = b;
    }


    public String getB() {
        return b;
    }

    public void setB(String b) {
        this.b = b;
    }

    public arduinoDSL_NodeDefinition getArduinodsl_nodedefinition() {
        return arduinodsl_nodedefinition;
    }

    public void setArduinodsl_nodedefinition(arduinoDSL_NodeDefinition arduinodsl_nodedefinition) {
        this.arduinodsl_nodedefinition = arduinodsl_nodedefinition;
    }

}
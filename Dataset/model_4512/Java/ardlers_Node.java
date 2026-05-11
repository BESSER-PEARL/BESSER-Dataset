





import java.util.List;
import java.util.ArrayList;

public class ardlers_Node  {

    private String name;





    private ardlers_BoardDefinition ardlers_boarddefinition;




    private ardlers_Attribute ardlers_attribute;


    public ardlers_Node(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ardlers_BoardDefinition getArdlers_boarddefinition() {
        return ardlers_boarddefinition;
    }

    public void setArdlers_boarddefinition(ardlers_BoardDefinition ardlers_boarddefinition) {
        this.ardlers_boarddefinition = ardlers_boarddefinition;
    }
    public ardlers_Attribute getArdlers_attribute() {
        return ardlers_attribute;
    }

    public void setArdlers_attribute(ardlers_Attribute ardlers_attribute) {
        this.ardlers_attribute = ardlers_attribute;
    }

}
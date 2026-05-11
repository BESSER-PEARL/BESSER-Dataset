





import java.util.List;
import java.util.ArrayList;

public class notation_NodeEntry  {

    private String value;





    private notation_Guide notation_guide;




    private notation_Node notation_node;


    public notation_NodeEntry(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public notation_Guide getNotation_guide() {
        return notation_guide;
    }

    public void setNotation_guide(notation_Guide notation_guide) {
        this.notation_guide = notation_guide;
    }
    public notation_Node getNotation_node() {
        return notation_node;
    }

    public void setNotation_node(notation_Node notation_node) {
        this.notation_node = notation_node;
    }

}
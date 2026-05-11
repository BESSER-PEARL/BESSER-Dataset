





import java.util.List;
import java.util.ArrayList;

public class notation_NodeEntry  {

    private String value;





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

    public notation_Node getNotation_node() {
        return notation_node;
    }

    public void setNotation_node(notation_Node notation_node) {
        this.notation_node = notation_node;
    }

}
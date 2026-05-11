





import java.util.List;
import java.util.ArrayList;

public class modeldraw_BooleanAttribute extends Item {

    private boolean negation;





    private modeldraw_Node modeldraw_node;


    public modeldraw_BooleanAttribute(
        boolean negation    ) {
        super(
        );
        this.negation = negation;
    }


    public boolean getNegation() {
        return negation;
    }

    public void setNegation(boolean negation) {
        this.negation = negation;
    }

    public modeldraw_Node getModeldraw_node() {
        return modeldraw_node;
    }

    public void setModeldraw_node(modeldraw_Node modeldraw_node) {
        this.modeldraw_node = modeldraw_node;
    }

}
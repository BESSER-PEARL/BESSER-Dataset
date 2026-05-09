





import java.util.List;
import java.util.ArrayList;

public class graphEditor_Variablenode extends Node {

    private String type;
    private boolean isKnown;
    private float values;



    public graphEditor_Variablenode(
        String type,        boolean isKnown,        float values    ) {
        super(
        );
        this.type = type;
        this.isKnown = isKnown;
        this.values = values;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getIsknown() {
        return isKnown;
    }

    public void setIsknown(boolean isKnown) {
        this.isKnown = isKnown;
    }
    public float getValues() {
        return values;
    }

    public void setValues(float values) {
        this.values = values;
    }


}






import java.util.List;
import java.util.ArrayList;

public class graphEditor_Variablenode extends Node {

    private boolean isKnown;
    private String type;
    private float values;



    public graphEditor_Variablenode(
        boolean isKnown,        String type,        float values    ) {
        super(
        );
        this.isKnown = isKnown;
        this.type = type;
        this.values = values;
    }


    public boolean getIsknown() {
        return isKnown;
    }

    public void setIsknown(boolean isKnown) {
        this.isKnown = isKnown;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public float getValues() {
        return values;
    }

    public void setValues(float values) {
        this.values = values;
    }


}
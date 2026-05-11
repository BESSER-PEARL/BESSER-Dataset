





import java.util.List;
import java.util.ArrayList;

public class graphEditor_Factornode extends Node {

    private String type;
    private String values;



    public graphEditor_Factornode(
        String type,        String values    ) {
        super(
        );
        this.type = type;
        this.values = values;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }


}
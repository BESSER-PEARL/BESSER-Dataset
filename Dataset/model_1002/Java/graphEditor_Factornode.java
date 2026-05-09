





import java.util.List;
import java.util.ArrayList;

public class graphEditor_Factornode extends Node {

    private String values;
    private String type;



    public graphEditor_Factornode(
        String values,        String type    ) {
        super(
        );
        this.values = values;
        this.type = type;
    }


    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}
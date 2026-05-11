





import java.util.List;
import java.util.ArrayList;

public class myDsl01_Attribute extends Property {

    private boolean optional;
    private String type;



    public myDsl01_Attribute(
        boolean optional,        String type    ) {
        super(
        );
        this.optional = optional;
        this.type = type;
    }


    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}
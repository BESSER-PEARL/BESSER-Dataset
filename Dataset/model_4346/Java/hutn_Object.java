





import java.util.List;
import java.util.ArrayList;

public class hutn_Object extends ModelElement {

    private String type;
    private String identifier;



    public hutn_Object(
        String type,        String identifier    ) {
        super(
        );
        this.type = type;
        this.identifier = identifier;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}
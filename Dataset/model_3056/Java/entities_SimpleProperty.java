





import java.util.List;
import java.util.ArrayList;

public class entities_SimpleProperty extends Property {

    private String type;



    public entities_SimpleProperty(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}






import java.util.List;
import java.util.ArrayList;

public class ER_Attribute extends Feature {

    private String type;



    public ER_Attribute(
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
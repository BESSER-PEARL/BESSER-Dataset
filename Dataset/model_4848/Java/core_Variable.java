





import java.util.List;
import java.util.ArrayList;

public class core_Variable extends IdentifiedElement {

    private String type;



    public core_Variable(
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
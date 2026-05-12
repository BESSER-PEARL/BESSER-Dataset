





import java.util.List;
import java.util.ArrayList;

public class model_component_Port extends INamedElement {

    private String type;



    public model_component_Port(
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
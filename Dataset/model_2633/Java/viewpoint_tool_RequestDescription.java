





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_RequestDescription extends AbstractToolDescription {

    private String type;



    public viewpoint_tool_RequestDescription(
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
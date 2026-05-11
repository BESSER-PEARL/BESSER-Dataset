





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_ChangeContext extends ContainerModelOperation {

    private String browseExpression;



    public viewpoint_tool_ChangeContext(
        String browseExpression    ) {
        super(
        );
        this.browseExpression = browseExpression;
    }


    public String getBrowseexpression() {
        return browseExpression;
    }

    public void setBrowseexpression(String browseExpression) {
        this.browseExpression = browseExpression;
    }


}
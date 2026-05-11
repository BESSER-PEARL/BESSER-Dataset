





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_RepresentationNavigationDescription extends AbstractToolDescription {

    private String browseExpression;
    private String navigationNameExpression;





    private RepresentationDescription representationdescription;


    public viewpoint_tool_RepresentationNavigationDescription(
        String browseExpression,        String navigationNameExpression    ) {
        super(
        );
        this.browseExpression = browseExpression;
        this.navigationNameExpression = navigationNameExpression;
    }


    public String getBrowseexpression() {
        return browseExpression;
    }

    public void setBrowseexpression(String browseExpression) {
        this.browseExpression = browseExpression;
    }
    public String getNavigationnameexpression() {
        return navigationNameExpression;
    }

    public void setNavigationnameexpression(String navigationNameExpression) {
        this.navigationNameExpression = navigationNameExpression;
    }

    public RepresentationDescription getRepresentationdescription() {
        return representationdescription;
    }

    public void setRepresentationdescription(RepresentationDescription representationdescription) {
        this.representationdescription = representationdescription;
    }

}
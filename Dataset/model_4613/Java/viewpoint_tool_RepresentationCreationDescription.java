





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_RepresentationCreationDescription extends AbstractToolDescription {

    private String browseExpression;
    private String titleExpression;





    private tool_InitialOperation tool_initialoperation;




    private RepresentationDescription representationdescription;


    public viewpoint_tool_RepresentationCreationDescription(
        String browseExpression,        String titleExpression    ) {
        super(
        );
        this.browseExpression = browseExpression;
        this.titleExpression = titleExpression;
    }


    public String getBrowseexpression() {
        return browseExpression;
    }

    public void setBrowseexpression(String browseExpression) {
        this.browseExpression = browseExpression;
    }
    public String getTitleexpression() {
        return titleExpression;
    }

    public void setTitleexpression(String titleExpression) {
        this.titleExpression = titleExpression;
    }

    public tool_InitialOperation getTool_initialoperation() {
        return tool_initialoperation;
    }

    public void setTool_initialoperation(tool_InitialOperation tool_initialoperation) {
        this.tool_initialoperation = tool_initialoperation;
    }
    public RepresentationDescription getRepresentationdescription() {
        return representationdescription;
    }

    public void setRepresentationdescription(RepresentationDescription representationdescription) {
        this.representationdescription = representationdescription;
    }

}
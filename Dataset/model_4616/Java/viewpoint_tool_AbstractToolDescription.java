





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_AbstractToolDescription extends ToolEntry {

    private boolean forceRefresh;
    private String precondition;



    public viewpoint_tool_AbstractToolDescription(
        boolean forceRefresh,        String precondition    ) {
        super(
        );
        this.forceRefresh = forceRefresh;
        this.precondition = precondition;
    }


    public boolean getForcerefresh() {
        return forceRefresh;
    }

    public void setForcerefresh(boolean forceRefresh) {
        this.forceRefresh = forceRefresh;
    }
    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }


}
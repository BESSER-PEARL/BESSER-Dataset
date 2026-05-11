





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_Preferences  {

    private String openNodes;
    private String openViews;
    private String id;
    private String enableTooltips;
    private String userId;
    private String themeId;
    private String selectedNode;
    private String selectedView;



    public org_sgiusa_model_Preferences(
        String openNodes,        String openViews,        String id,        String enableTooltips,        String userId,        String themeId,        String selectedNode,        String selectedView    ) {
        this.openNodes = openNodes;
        this.openViews = openViews;
        this.id = id;
        this.enableTooltips = enableTooltips;
        this.userId = userId;
        this.themeId = themeId;
        this.selectedNode = selectedNode;
        this.selectedView = selectedView;
    }


    public String getOpennodes() {
        return openNodes;
    }

    public void setOpennodes(String openNodes) {
        this.openNodes = openNodes;
    }
    public String getOpenviews() {
        return openViews;
    }

    public void setOpenviews(String openViews) {
        this.openViews = openViews;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getEnabletooltips() {
        return enableTooltips;
    }

    public void setEnabletooltips(String enableTooltips) {
        this.enableTooltips = enableTooltips;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getThemeid() {
        return themeId;
    }

    public void setThemeid(String themeId) {
        this.themeId = themeId;
    }
    public String getSelectednode() {
        return selectedNode;
    }

    public void setSelectednode(String selectedNode) {
        this.selectedNode = selectedNode;
    }
    public String getSelectedview() {
        return selectedView;
    }

    public void setSelectedview(String selectedView) {
        this.selectedView = selectedView;
    }


}
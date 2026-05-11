





import java.util.List;
import java.util.ArrayList;

public class ccore_ViewLinkType  {

    private String displayCreate;
    private boolean canCreateLink;
    private boolean canCreateItem;
    private boolean aggregation;





    private ccore_ViewItemType ccore_viewitemtype;


    public ccore_ViewLinkType(
        String displayCreate,        boolean canCreateLink,        boolean canCreateItem,        boolean aggregation    ) {
        this.displayCreate = displayCreate;
        this.canCreateLink = canCreateLink;
        this.canCreateItem = canCreateItem;
        this.aggregation = aggregation;
    }


    public String getDisplaycreate() {
        return displayCreate;
    }

    public void setDisplaycreate(String displayCreate) {
        this.displayCreate = displayCreate;
    }
    public boolean getCancreatelink() {
        return canCreateLink;
    }

    public void setCancreatelink(boolean canCreateLink) {
        this.canCreateLink = canCreateLink;
    }
    public boolean getCancreateitem() {
        return canCreateItem;
    }

    public void setCancreateitem(boolean canCreateItem) {
        this.canCreateItem = canCreateItem;
    }
    public boolean getAggregation() {
        return aggregation;
    }

    public void setAggregation(boolean aggregation) {
        this.aggregation = aggregation;
    }

    public ccore_ViewItemType getCcore_viewitemtype() {
        return ccore_viewitemtype;
    }

    public void setCcore_viewitemtype(ccore_ViewItemType ccore_viewitemtype) {
        this.ccore_viewitemtype = ccore_viewitemtype;
    }

}
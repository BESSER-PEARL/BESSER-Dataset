





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_AbstractToolDescription extends ToolEntry {

    private boolean inverseSelectionOrder;
    private String precondition;
    private boolean forceRefresh;
    private String elementsToSelect;



    public viewpoint_tool_AbstractToolDescription(
        boolean inverseSelectionOrder,        String precondition,        boolean forceRefresh,        String elementsToSelect    ) {
        super(
        );
        this.inverseSelectionOrder = inverseSelectionOrder;
        this.precondition = precondition;
        this.forceRefresh = forceRefresh;
        this.elementsToSelect = elementsToSelect;
    }


    public boolean getInverseselectionorder() {
        return inverseSelectionOrder;
    }

    public void setInverseselectionorder(boolean inverseSelectionOrder) {
        this.inverseSelectionOrder = inverseSelectionOrder;
    }
    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }
    public boolean getForcerefresh() {
        return forceRefresh;
    }

    public void setForcerefresh(boolean forceRefresh) {
        this.forceRefresh = forceRefresh;
    }
    public String getElementstoselect() {
        return elementsToSelect;
    }

    public void setElementstoselect(String elementsToSelect) {
        this.elementsToSelect = elementsToSelect;
    }


}
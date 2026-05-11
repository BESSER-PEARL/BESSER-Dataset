





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_AbstractToolDescription extends ToolEntry {

    private boolean inverseSelectionOrder;
    private String precondition;
    private String elementsToSelect;
    private boolean forceRefresh;



    public viewpoint_tool_AbstractToolDescription(
        boolean inverseSelectionOrder,        String precondition,        String elementsToSelect,        boolean forceRefresh    ) {
        super(
        );
        this.inverseSelectionOrder = inverseSelectionOrder;
        this.precondition = precondition;
        this.elementsToSelect = elementsToSelect;
        this.forceRefresh = forceRefresh;
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
    public String getElementstoselect() {
        return elementsToSelect;
    }

    public void setElementstoselect(String elementsToSelect) {
        this.elementsToSelect = elementsToSelect;
    }
    public boolean getForcerefresh() {
        return forceRefresh;
    }

    public void setForcerefresh(boolean forceRefresh) {
        this.forceRefresh = forceRefresh;
    }


}
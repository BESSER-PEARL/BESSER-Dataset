





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_AbstractToolDescription extends ToolEntry {

    private boolean forceRefresh;
    private String precondition;
    private String elementsToSelect;
    private boolean inverseSelectionOrder;



    public viewpoint_tool_AbstractToolDescription(
        boolean forceRefresh,        String precondition,        String elementsToSelect,        boolean inverseSelectionOrder    ) {
        super(
        );
        this.forceRefresh = forceRefresh;
        this.precondition = precondition;
        this.elementsToSelect = elementsToSelect;
        this.inverseSelectionOrder = inverseSelectionOrder;
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
    public String getElementstoselect() {
        return elementsToSelect;
    }

    public void setElementstoselect(String elementsToSelect) {
        this.elementsToSelect = elementsToSelect;
    }
    public boolean getInverseselectionorder() {
        return inverseSelectionOrder;
    }

    public void setInverseselectionorder(boolean inverseSelectionOrder) {
        this.inverseSelectionOrder = inverseSelectionOrder;
    }


}
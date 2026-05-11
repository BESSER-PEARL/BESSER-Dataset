





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_AbstractToolDescription extends ToolEntry {

    private boolean forceRefresh;
    private boolean inverseSelectionOrder;
    private String precondition;
    private String elementsToSelect;





    private List<tool_ToolFilterDescription> tool_toolfilterdescriptions;


    public viewpoint_tool_AbstractToolDescription(
        boolean forceRefresh,        boolean inverseSelectionOrder,        String precondition,        String elementsToSelect    ) {
        super(
        );
        this.forceRefresh = forceRefresh;
        this.inverseSelectionOrder = inverseSelectionOrder;
        this.precondition = precondition;
        this.elementsToSelect = elementsToSelect;
        this.tool_toolfilterdescriptions = new ArrayList<>();
    }

    public viewpoint_tool_AbstractToolDescription(
        boolean forceRefresh,        boolean inverseSelectionOrder,        String precondition,        String elementsToSelect        ArrayList<tool_ToolFilterDescription> tool_toolfilterdescriptions    ) {
        this.forceRefresh = forceRefresh;
        this.inverseSelectionOrder = inverseSelectionOrder;
        this.precondition = precondition;
        this.elementsToSelect = elementsToSelect;
        this.tool_toolfilterdescriptions = tool_toolfilterdescriptions;
    }

    public boolean getForcerefresh() {
        return forceRefresh;
    }

    public void setForcerefresh(boolean forceRefresh) {
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

    public List<tool_ToolFilterDescription> getTool_toolfilterdescriptions() {
        return tool_toolfilterdescriptions;
    }

    public void addTool_toolfilterdescription(Tool_toolfilterdescription tool_toolfilterdescription) {
        this.tool_toolfilterdescriptions.add(tool_toolfilterdescription);
    }

}
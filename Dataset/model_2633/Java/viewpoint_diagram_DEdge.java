





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_DEdge extends diagram_EdgeTarget, diagram_DDiagramElement {

    private String size;
    private boolean isFold;
    private String beginLabel;
    private String arrangeConstraints;
    private String routingStyle;
    private boolean isMockEdge;
    private String endLabel;





    private List<EdgeTarget> edgetargets;




    private EdgeTarget edgetarget;




    private diagram_viewpoint_Style diagram_viewpoint_style;




    private EdgeTarget edgetarget;


    public viewpoint_diagram_DEdge(
        String size,        boolean isFold,        String beginLabel,        String arrangeConstraints,        String routingStyle,        boolean isMockEdge,        String endLabel    ) {
        super(
        );
        this.size = size;
        this.isFold = isFold;
        this.beginLabel = beginLabel;
        this.arrangeConstraints = arrangeConstraints;
        this.routingStyle = routingStyle;
        this.isMockEdge = isMockEdge;
        this.endLabel = endLabel;
        this.edgetargets = new ArrayList<>();
    }

    public viewpoint_diagram_DEdge(
        String size,        boolean isFold,        String beginLabel,        String arrangeConstraints,        String routingStyle,        boolean isMockEdge,        String endLabel        ArrayList<EdgeTarget> edgetargets    ) {
        this.size = size;
        this.isFold = isFold;
        this.beginLabel = beginLabel;
        this.arrangeConstraints = arrangeConstraints;
        this.routingStyle = routingStyle;
        this.isMockEdge = isMockEdge;
        this.endLabel = endLabel;
        this.edgetargets = edgetargets;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public boolean getIsfold() {
        return isFold;
    }

    public void setIsfold(boolean isFold) {
        this.isFold = isFold;
    }
    public String getBeginlabel() {
        return beginLabel;
    }

    public void setBeginlabel(String beginLabel) {
        this.beginLabel = beginLabel;
    }
    public String getArrangeconstraints() {
        return arrangeConstraints;
    }

    public void setArrangeconstraints(String arrangeConstraints) {
        this.arrangeConstraints = arrangeConstraints;
    }
    public String getRoutingstyle() {
        return routingStyle;
    }

    public void setRoutingstyle(String routingStyle) {
        this.routingStyle = routingStyle;
    }
    public boolean getIsmockedge() {
        return isMockEdge;
    }

    public void setIsmockedge(boolean isMockEdge) {
        this.isMockEdge = isMockEdge;
    }
    public String getEndlabel() {
        return endLabel;
    }

    public void setEndlabel(String endLabel) {
        this.endLabel = endLabel;
    }

    public List<EdgeTarget> getEdgetargets() {
        return edgetargets;
    }

    public void addEdgetarget(Edgetarget edgetarget) {
        this.edgetargets.add(edgetarget);
    }
    public EdgeTarget getEdgetarget() {
        return edgetarget;
    }

    public void setEdgetarget(EdgeTarget edgetarget) {
        this.edgetarget = edgetarget;
    }
    public diagram_viewpoint_Style getDiagram_viewpoint_style() {
        return diagram_viewpoint_style;
    }

    public void setDiagram_viewpoint_style(diagram_viewpoint_Style diagram_viewpoint_style) {
        this.diagram_viewpoint_style = diagram_viewpoint_style;
    }
    public EdgeTarget getEdgetarget() {
        return edgetarget;
    }

    public void setEdgetarget(EdgeTarget edgetarget) {
        this.edgetarget = edgetarget;
    }

}






import java.util.List;
import java.util.ArrayList;

public class diagram_DEdge extends EdgeTarget, DDiagramElement {

    private String size;
    private String arrangeConstraints;
    private String routingStyle;
    private boolean isFold;
    private boolean isMockEdge;
    private String endLabel;
    private String beginLabel;





    private diagram_DDiagram diagram_ddiagram;


    public diagram_DEdge(
        String size,        String arrangeConstraints,        String routingStyle,        boolean isFold,        boolean isMockEdge,        String endLabel,        String beginLabel    ) {
        super(
        );
        this.size = size;
        this.arrangeConstraints = arrangeConstraints;
        this.routingStyle = routingStyle;
        this.isFold = isFold;
        this.isMockEdge = isMockEdge;
        this.endLabel = endLabel;
        this.beginLabel = beginLabel;
    }


    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
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
    public boolean getIsfold() {
        return isFold;
    }

    public void setIsfold(boolean isFold) {
        this.isFold = isFold;
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
    public String getBeginlabel() {
        return beginLabel;
    }

    public void setBeginlabel(String beginLabel) {
        this.beginLabel = beginLabel;
    }

    public diagram_DDiagram getDiagram_ddiagram() {
        return diagram_ddiagram;
    }

    public void setDiagram_ddiagram(diagram_DDiagram diagram_ddiagram) {
        this.diagram_ddiagram = diagram_ddiagram;
    }

}
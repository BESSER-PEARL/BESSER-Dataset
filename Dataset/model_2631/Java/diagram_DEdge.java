





import java.util.List;
import java.util.ArrayList;

public class diagram_DEdge extends EdgeTarget, DDiagramElement {

    private String beginLabel;
    private String arrangeConstraints;
    private String size;
    private boolean isMockEdge;
    private boolean isFold;
    private String routingStyle;
    private String endLabel;





    private diagram_DDiagram diagram_ddiagram;


    public diagram_DEdge(
        String beginLabel,        String arrangeConstraints,        String size,        boolean isMockEdge,        boolean isFold,        String routingStyle,        String endLabel    ) {
        super(
        );
        this.beginLabel = beginLabel;
        this.arrangeConstraints = arrangeConstraints;
        this.size = size;
        this.isMockEdge = isMockEdge;
        this.isFold = isFold;
        this.routingStyle = routingStyle;
        this.endLabel = endLabel;
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
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public boolean getIsmockedge() {
        return isMockEdge;
    }

    public void setIsmockedge(boolean isMockEdge) {
        this.isMockEdge = isMockEdge;
    }
    public boolean getIsfold() {
        return isFold;
    }

    public void setIsfold(boolean isFold) {
        this.isFold = isFold;
    }
    public String getRoutingstyle() {
        return routingStyle;
    }

    public void setRoutingstyle(String routingStyle) {
        this.routingStyle = routingStyle;
    }
    public String getEndlabel() {
        return endLabel;
    }

    public void setEndlabel(String endLabel) {
        this.endLabel = endLabel;
    }

    public diagram_DDiagram getDiagram_ddiagram() {
        return diagram_ddiagram;
    }

    public void setDiagram_ddiagram(diagram_DDiagram diagram_ddiagram) {
        this.diagram_ddiagram = diagram_ddiagram;
    }

}
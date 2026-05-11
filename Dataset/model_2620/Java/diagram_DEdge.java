





import java.util.List;
import java.util.ArrayList;

public class diagram_DEdge extends EdgeTarget, DDiagramElement {

    private boolean isMockEdge;
    private String routingStyle;
    private String beginLabel;
    private String arrangeConstraints;
    private boolean isFold;
    private String endLabel;
    private String size;





    private diagram_DDiagram diagram_ddiagram;


    public diagram_DEdge(
        boolean isMockEdge,        String routingStyle,        String beginLabel,        String arrangeConstraints,        boolean isFold,        String endLabel,        String size    ) {
        super(
        );
        this.isMockEdge = isMockEdge;
        this.routingStyle = routingStyle;
        this.beginLabel = beginLabel;
        this.arrangeConstraints = arrangeConstraints;
        this.isFold = isFold;
        this.endLabel = endLabel;
        this.size = size;
    }


    public boolean getIsmockedge() {
        return isMockEdge;
    }

    public void setIsmockedge(boolean isMockEdge) {
        this.isMockEdge = isMockEdge;
    }
    public String getRoutingstyle() {
        return routingStyle;
    }

    public void setRoutingstyle(String routingStyle) {
        this.routingStyle = routingStyle;
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
    public boolean getIsfold() {
        return isFold;
    }

    public void setIsfold(boolean isFold) {
        this.isFold = isFold;
    }
    public String getEndlabel() {
        return endLabel;
    }

    public void setEndlabel(String endLabel) {
        this.endLabel = endLabel;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public diagram_DDiagram getDiagram_ddiagram() {
        return diagram_ddiagram;
    }

    public void setDiagram_ddiagram(diagram_DDiagram diagram_ddiagram) {
        this.diagram_ddiagram = diagram_ddiagram;
    }

}
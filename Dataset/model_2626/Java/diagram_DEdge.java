





import java.util.List;
import java.util.ArrayList;

public class diagram_DEdge extends EdgeTarget, DDiagramElement {

    private String routingStyle;
    private String endLabel;
    private boolean isMockEdge;
    private String size;
    private String beginLabel;
    private boolean isFold;
    private String arrangeConstraints;





    private diagram_DDiagram diagram_ddiagram;


    public diagram_DEdge(
        String routingStyle,        String endLabel,        boolean isMockEdge,        String size,        String beginLabel,        boolean isFold,        String arrangeConstraints    ) {
        super(
        );
        this.routingStyle = routingStyle;
        this.endLabel = endLabel;
        this.isMockEdge = isMockEdge;
        this.size = size;
        this.beginLabel = beginLabel;
        this.isFold = isFold;
        this.arrangeConstraints = arrangeConstraints;
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
    public boolean getIsmockedge() {
        return isMockEdge;
    }

    public void setIsmockedge(boolean isMockEdge) {
        this.isMockEdge = isMockEdge;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getBeginlabel() {
        return beginLabel;
    }

    public void setBeginlabel(String beginLabel) {
        this.beginLabel = beginLabel;
    }
    public boolean getIsfold() {
        return isFold;
    }

    public void setIsfold(boolean isFold) {
        this.isFold = isFold;
    }
    public String getArrangeconstraints() {
        return arrangeConstraints;
    }

    public void setArrangeconstraints(String arrangeConstraints) {
        this.arrangeConstraints = arrangeConstraints;
    }

    public diagram_DDiagram getDiagram_ddiagram() {
        return diagram_ddiagram;
    }

    public void setDiagram_ddiagram(diagram_DDiagram diagram_ddiagram) {
        this.diagram_ddiagram = diagram_ddiagram;
    }

}
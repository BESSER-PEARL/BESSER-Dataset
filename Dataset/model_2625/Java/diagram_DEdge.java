





import java.util.List;
import java.util.ArrayList;

public class diagram_DEdge extends EdgeTarget, DDiagramElement {

    private String size;
    private String beginLabel;
    private String endLabel;
    private String routingStyle;
    private boolean isMockEdge;
    private boolean isFold;
    private String arrangeConstraints;





    private diagram_DDiagram diagram_ddiagram;


    public diagram_DEdge(
        String size,        String beginLabel,        String endLabel,        String routingStyle,        boolean isMockEdge,        boolean isFold,        String arrangeConstraints    ) {
        super(
        );
        this.size = size;
        this.beginLabel = beginLabel;
        this.endLabel = endLabel;
        this.routingStyle = routingStyle;
        this.isMockEdge = isMockEdge;
        this.isFold = isFold;
        this.arrangeConstraints = arrangeConstraints;
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
    public String getEndlabel() {
        return endLabel;
    }

    public void setEndlabel(String endLabel) {
        this.endLabel = endLabel;
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
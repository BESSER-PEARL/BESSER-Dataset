





import java.util.List;
import java.util.ArrayList;

public class diagram_DEdge extends EdgeTarget, DDiagramElement {

    private boolean isFold;
    private String arrangeConstraints;
    private String endLabel;
    private boolean isMockEdge;
    private String beginLabel;
    private String size;
    private String routingStyle;





    private diagram_DDiagram diagram_ddiagram;


    public diagram_DEdge(
        boolean isFold,        String arrangeConstraints,        String endLabel,        boolean isMockEdge,        String beginLabel,        String size,        String routingStyle    ) {
        super(
        );
        this.isFold = isFold;
        this.arrangeConstraints = arrangeConstraints;
        this.endLabel = endLabel;
        this.isMockEdge = isMockEdge;
        this.beginLabel = beginLabel;
        this.size = size;
        this.routingStyle = routingStyle;
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
    public String getBeginlabel() {
        return beginLabel;
    }

    public void setBeginlabel(String beginLabel) {
        this.beginLabel = beginLabel;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getRoutingstyle() {
        return routingStyle;
    }

    public void setRoutingstyle(String routingStyle) {
        this.routingStyle = routingStyle;
    }

    public diagram_DDiagram getDiagram_ddiagram() {
        return diagram_ddiagram;
    }

    public void setDiagram_ddiagram(diagram_DDiagram diagram_ddiagram) {
        this.diagram_ddiagram = diagram_ddiagram;
    }

}
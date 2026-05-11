





import java.util.List;
import java.util.ArrayList;

public class diagram_NodeStyle extends HideLabelCapabilityStyle, BorderedStyle, LabelStyle, Style {

    private String labelPosition;
    private String labelDirection;





    private diagram_DNodeListElement diagram_dnodelistelement;




    private diagram_DNode diagram_dnode;


    public diagram_NodeStyle(
        String labelPosition,        String labelDirection    ) {
        super(
        );
        this.labelPosition = labelPosition;
        this.labelDirection = labelDirection;
    }


    public String getLabelposition() {
        return labelPosition;
    }

    public void setLabelposition(String labelPosition) {
        this.labelPosition = labelPosition;
    }
    public String getLabeldirection() {
        return labelDirection;
    }

    public void setLabeldirection(String labelDirection) {
        this.labelDirection = labelDirection;
    }

    public diagram_DNodeListElement getDiagram_dnodelistelement() {
        return diagram_dnodelistelement;
    }

    public void setDiagram_dnodelistelement(diagram_DNodeListElement diagram_dnodelistelement) {
        this.diagram_dnodelistelement = diagram_dnodelistelement;
    }
    public diagram_DNode getDiagram_dnode() {
        return diagram_dnode;
    }

    public void setDiagram_dnode(diagram_DNode diagram_dnode) {
        this.diagram_dnode = diagram_dnode;
    }

}
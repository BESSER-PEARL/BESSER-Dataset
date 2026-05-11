





import java.util.List;
import java.util.ArrayList;

public class diagram_NodeStyle extends LabelStyle, HideLabelCapabilityStyle, BorderedStyle, Style {

    private String labelPosition;





    private diagram_DNodeListElement diagram_dnodelistelement;




    private diagram_DNode diagram_dnode;


    public diagram_NodeStyle(
        String labelPosition    ) {
        super(
        );
        this.labelPosition = labelPosition;
    }


    public String getLabelposition() {
        return labelPosition;
    }

    public void setLabelposition(String labelPosition) {
        this.labelPosition = labelPosition;
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
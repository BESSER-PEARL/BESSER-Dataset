





import java.util.List;
import java.util.ArrayList;

public class diagram_NodeStyle extends Style, LabelStyle, BorderedStyle {

    private boolean hideLabelByDefault;
    private String labelPosition;





    private diagram_DNodeListElement diagram_dnodelistelement;




    private diagram_DNode diagram_dnode;


    public diagram_NodeStyle(
        boolean hideLabelByDefault,        String labelPosition    ) {
        super(
        );
        this.hideLabelByDefault = hideLabelByDefault;
        this.labelPosition = labelPosition;
    }


    public boolean getHidelabelbydefault() {
        return hideLabelByDefault;
    }

    public void setHidelabelbydefault(boolean hideLabelByDefault) {
        this.hideLabelByDefault = hideLabelByDefault;
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
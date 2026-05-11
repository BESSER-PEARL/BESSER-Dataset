





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_TrgStatement extends TrgModElement {

    private String atts;
    private String label;



    public jointPackage_Ecore2Maude_TrgStatement(
        String atts,        String label    ) {
        super(
        );
        this.atts = atts;
        this.label = label;
    }


    public String getAtts() {
        return atts;
    }

    public void setAtts(String atts) {
        this.atts = atts;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}






import java.util.List;
import java.util.ArrayList;

public class Maude_Statement extends ModElement {

    private String label;
    private String atts;



    public Maude_Statement(
        String label,        String atts    ) {
        super(
        );
        this.label = label;
        this.atts = atts;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getAtts() {
        return atts;
    }

    public void setAtts(String atts) {
        this.atts = atts;
    }


}
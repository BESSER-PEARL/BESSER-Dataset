





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_BorderLayoutData extends LayoutData {

    private boolean vertical;
    private String alignment;



    public gmf_all_gmfgraph_BorderLayoutData(
        boolean vertical,        String alignment    ) {
        super(
        );
        this.vertical = vertical;
        this.alignment = alignment;
    }


    public boolean getVertical() {
        return vertical;
    }

    public void setVertical(boolean vertical) {
        this.vertical = vertical;
    }
    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }


}
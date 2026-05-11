





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_BorderLayoutData extends LayoutData {

    private String alignment;
    private boolean vertical;



    public gmfgraph_BorderLayoutData(
        String alignment,        boolean vertical    ) {
        super(
        );
        this.alignment = alignment;
        this.vertical = vertical;
    }


    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }
    public boolean getVertical() {
        return vertical;
    }

    public void setVertical(boolean vertical) {
        this.vertical = vertical;
    }


}
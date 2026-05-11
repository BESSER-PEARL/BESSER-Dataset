





import java.util.List;
import java.util.ArrayList;

public class WT_Port  {

    private String label;
    private boolean isPublic;





    private WT_Component wt_component;


    public WT_Port(
        String label,        boolean isPublic    ) {
        this.label = label;
        this.isPublic = isPublic;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public boolean getIspublic() {
        return isPublic;
    }

    public void setIspublic(boolean isPublic) {
        this.isPublic = isPublic;
    }

    public WT_Component getWt_component() {
        return wt_component;
    }

    public void setWt_component(WT_Component wt_component) {
        this.wt_component = wt_component;
    }

}






import java.util.List;
import java.util.ArrayList;

public class WT_Component  {

    private String label;





    private WT_Architecture wt_architecture;


    public WT_Component(
        String label    ) {
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public WT_Architecture getWt_architecture() {
        return wt_architecture;
    }

    public void setWt_architecture(WT_Architecture wt_architecture) {
        this.wt_architecture = wt_architecture;
    }

}
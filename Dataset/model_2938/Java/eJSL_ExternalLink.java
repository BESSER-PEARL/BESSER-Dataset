





import java.util.List;
import java.util.ArrayList;

public class eJSL_ExternalLink extends Link {

    private String target;
    private String label;



    public eJSL_ExternalLink(
        String target,        String label    ) {
        super(
        );
        this.target = target;
        this.label = label;
    }


    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}
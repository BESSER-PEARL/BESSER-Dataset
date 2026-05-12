





import java.util.List;
import java.util.ArrayList;

public class XHTML_Table extends Attrs, block, ButtonContent {

    private String frame;
    private String rules;



    public XHTML_Table(
        String frame,        String rules    ) {
        super(
        );
        this.frame = frame;
        this.rules = rules;
    }


    public String getFrame() {
        return frame;
    }

    public void setFrame(String frame) {
        this.frame = frame;
    }
    public String getRules() {
        return rules;
    }

    public void setRules(String rules) {
        this.rules = rules;
    }


}
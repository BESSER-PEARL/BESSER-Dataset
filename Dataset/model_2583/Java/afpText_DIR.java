





import java.util.List;
import java.util.ArrayList;

public class afpText_DIR extends triplet {

    private String RLENGTH;
    private String RWIDTHFRACTION;
    private String RWIDTH;



    public afpText_DIR(
        String RLENGTH,        String RWIDTHFRACTION,        String RWIDTH    ) {
        super(
        );
        this.RLENGTH = RLENGTH;
        this.RWIDTHFRACTION = RWIDTHFRACTION;
        this.RWIDTH = RWIDTH;
    }


    public String getRlength() {
        return RLENGTH;
    }

    public void setRlength(String RLENGTH) {
        this.RLENGTH = RLENGTH;
    }
    public String getRwidthfraction() {
        return RWIDTHFRACTION;
    }

    public void setRwidthfraction(String RWIDTHFRACTION) {
        this.RWIDTHFRACTION = RWIDTHFRACTION;
    }
    public String getRwidth() {
        return RWIDTH;
    }

    public void setRwidth(String RWIDTH) {
        this.RWIDTH = RWIDTH;
    }


}
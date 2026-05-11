





import java.util.List;
import java.util.ArrayList;

public class afpText_DBR extends triplet {

    private String RWIDTH;
    private String RLENGTH;
    private String RWIDTHFRACTION;



    public afpText_DBR(
        String RWIDTH,        String RLENGTH,        String RWIDTHFRACTION    ) {
        super(
        );
        this.RWIDTH = RWIDTH;
        this.RLENGTH = RLENGTH;
        this.RWIDTHFRACTION = RWIDTHFRACTION;
    }


    public String getRwidth() {
        return RWIDTH;
    }

    public void setRwidth(String RWIDTH) {
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


}
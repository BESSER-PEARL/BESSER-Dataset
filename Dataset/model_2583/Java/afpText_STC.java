





import java.util.List;
import java.util.ArrayList;

public class afpText_STC extends triplet {

    private String FRGCOLOR;
    private String PRECSION;



    public afpText_STC(
        String FRGCOLOR,        String PRECSION    ) {
        super(
        );
        this.FRGCOLOR = FRGCOLOR;
        this.PRECSION = PRECSION;
    }


    public String getFrgcolor() {
        return FRGCOLOR;
    }

    public void setFrgcolor(String FRGCOLOR) {
        this.FRGCOLOR = FRGCOLOR;
    }
    public String getPrecsion() {
        return PRECSION;
    }

    public void setPrecsion(String PRECSION) {
        this.PRECSION = PRECSION;
    }


}
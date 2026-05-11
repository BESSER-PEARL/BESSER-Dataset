





import java.util.List;
import java.util.ArrayList;

public class afpText_OVS extends triplet {

    private String BYPSIDEN;
    private String OVERCHAR;



    public afpText_OVS(
        String BYPSIDEN,        String OVERCHAR    ) {
        super(
        );
        this.BYPSIDEN = BYPSIDEN;
        this.OVERCHAR = OVERCHAR;
    }


    public String getBypsiden() {
        return BYPSIDEN;
    }

    public void setBypsiden(String BYPSIDEN) {
        this.BYPSIDEN = BYPSIDEN;
    }
    public String getOverchar() {
        return OVERCHAR;
    }

    public void setOverchar(String OVERCHAR) {
        this.OVERCHAR = OVERCHAR;
    }


}
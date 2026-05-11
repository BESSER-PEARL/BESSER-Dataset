





import java.util.List;
import java.util.ArrayList;

public class afpText_GSCH extends triplet {

    private String HY;
    private String HX;



    public afpText_GSCH(
        String HY,        String HX    ) {
        super(
        );
        this.HY = HY;
        this.HX = HX;
    }


    public String getHy() {
        return HY;
    }

    public void setHy(String HY) {
        this.HY = HY;
    }
    public String getHx() {
        return HX;
    }

    public void setHx(String HX) {
        this.HX = HX;
    }


}
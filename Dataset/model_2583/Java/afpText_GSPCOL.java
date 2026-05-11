





import java.util.List;
import java.util.ArrayList;

public class afpText_GSPCOL extends triplet {

    private String RES1;
    private String RES2;
    private String COLSIZE3;
    private String COLSIZE4;
    private String COLSIZE2;
    private String COLSPCE;
    private String COLVALUE;
    private String COLSIZE1;



    public afpText_GSPCOL(
        String RES1,        String RES2,        String COLSIZE3,        String COLSIZE4,        String COLSIZE2,        String COLSPCE,        String COLVALUE,        String COLSIZE1    ) {
        super(
        );
        this.RES1 = RES1;
        this.RES2 = RES2;
        this.COLSIZE3 = COLSIZE3;
        this.COLSIZE4 = COLSIZE4;
        this.COLSIZE2 = COLSIZE2;
        this.COLSPCE = COLSPCE;
        this.COLVALUE = COLVALUE;
        this.COLSIZE1 = COLSIZE1;
    }


    public String getRes1() {
        return RES1;
    }

    public void setRes1(String RES1) {
        this.RES1 = RES1;
    }
    public String getRes2() {
        return RES2;
    }

    public void setRes2(String RES2) {
        this.RES2 = RES2;
    }
    public String getColsize3() {
        return COLSIZE3;
    }

    public void setColsize3(String COLSIZE3) {
        this.COLSIZE3 = COLSIZE3;
    }
    public String getColsize4() {
        return COLSIZE4;
    }

    public void setColsize4(String COLSIZE4) {
        this.COLSIZE4 = COLSIZE4;
    }
    public String getColsize2() {
        return COLSIZE2;
    }

    public void setColsize2(String COLSIZE2) {
        this.COLSIZE2 = COLSIZE2;
    }
    public String getColspce() {
        return COLSPCE;
    }

    public void setColspce(String COLSPCE) {
        this.COLSPCE = COLSPCE;
    }
    public String getColvalue() {
        return COLVALUE;
    }

    public void setColvalue(String COLVALUE) {
        this.COLVALUE = COLVALUE;
    }
    public String getColsize1() {
        return COLSIZE1;
    }

    public void setColsize1(String COLSIZE1) {
        this.COLSIZE1 = COLSIZE1;
    }


}
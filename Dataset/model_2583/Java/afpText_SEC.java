





import java.util.List;
import java.util.ArrayList;

public class afpText_SEC extends triplet {

    private String COLSIZE1;
    private String COLSIZE4;
    private String COLSIZE3;
    private String COLSPCE;
    private String COLSIZE2;
    private String COLVALUE;
    private String RESERVED;



    public afpText_SEC(
        String COLSIZE1,        String COLSIZE4,        String COLSIZE3,        String COLSPCE,        String COLSIZE2,        String COLVALUE,        String RESERVED    ) {
        super(
        );
        this.COLSIZE1 = COLSIZE1;
        this.COLSIZE4 = COLSIZE4;
        this.COLSIZE3 = COLSIZE3;
        this.COLSPCE = COLSPCE;
        this.COLSIZE2 = COLSIZE2;
        this.COLVALUE = COLVALUE;
        this.RESERVED = RESERVED;
    }


    public String getColsize1() {
        return COLSIZE1;
    }

    public void setColsize1(String COLSIZE1) {
        this.COLSIZE1 = COLSIZE1;
    }
    public String getColsize4() {
        return COLSIZE4;
    }

    public void setColsize4(String COLSIZE4) {
        this.COLSIZE4 = COLSIZE4;
    }
    public String getColsize3() {
        return COLSIZE3;
    }

    public void setColsize3(String COLSIZE3) {
        this.COLSIZE3 = COLSIZE3;
    }
    public String getColspce() {
        return COLSPCE;
    }

    public void setColspce(String COLSPCE) {
        this.COLSPCE = COLSPCE;
    }
    public String getColsize2() {
        return COLSIZE2;
    }

    public void setColsize2(String COLSIZE2) {
        this.COLSIZE2 = COLSIZE2;
    }
    public String getColvalue() {
        return COLVALUE;
    }

    public void setColvalue(String COLVALUE) {
        this.COLVALUE = COLVALUE;
    }
    public String getReserved() {
        return RESERVED;
    }

    public void setReserved(String RESERVED) {
        this.RESERVED = RESERVED;
    }


}
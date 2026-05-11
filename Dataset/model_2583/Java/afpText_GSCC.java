





import java.util.List;
import java.util.ArrayList;

public class afpText_GSCC extends triplet {

    private String CELLWI;
    private String CELLHI;
    private String CELLHFR;
    private String CELLWFR;



    public afpText_GSCC(
        String CELLWI,        String CELLHI,        String CELLHFR,        String CELLWFR    ) {
        super(
        );
        this.CELLWI = CELLWI;
        this.CELLHI = CELLHI;
        this.CELLHFR = CELLHFR;
        this.CELLWFR = CELLWFR;
    }


    public String getCellwi() {
        return CELLWI;
    }

    public void setCellwi(String CELLWI) {
        this.CELLWI = CELLWI;
    }
    public String getCellhi() {
        return CELLHI;
    }

    public void setCellhi(String CELLHI) {
        this.CELLHI = CELLHI;
    }
    public String getCellhfr() {
        return CELLHFR;
    }

    public void setCellhfr(String CELLHFR) {
        this.CELLHFR = CELLHFR;
    }
    public String getCellwfr() {
        return CELLWFR;
    }

    public void setCellwfr(String CELLWFR) {
        this.CELLWFR = CELLWFR;
    }


}
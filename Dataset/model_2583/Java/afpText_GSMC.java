





import java.util.List;
import java.util.ArrayList;

public class afpText_GSMC extends triplet {

    private String CELLHI;
    private String CELLWI;



    public afpText_GSMC(
        String CELLHI,        String CELLWI    ) {
        super(
        );
        this.CELLHI = CELLHI;
        this.CELLWI = CELLWI;
    }


    public String getCellhi() {
        return CELLHI;
    }

    public void setCellhi(String CELLHI) {
        this.CELLHI = CELLHI;
    }
    public String getCellwi() {
        return CELLWI;
    }

    public void setCellwi(String CELLWI) {
        this.CELLWI = CELLWI;
    }


}






import java.util.List;
import java.util.ArrayList;

public class umm_BBIE extends ABIEProperty {

    private String fixedValue;
    private String restriction;





    private umm_BDT umm_bdt;


    public umm_BBIE(
        String fixedValue,        String restriction    ) {
        super(
        );
        this.fixedValue = fixedValue;
        this.restriction = restriction;
    }


    public String getFixedvalue() {
        return fixedValue;
    }

    public void setFixedvalue(String fixedValue) {
        this.fixedValue = fixedValue;
    }
    public String getRestriction() {
        return restriction;
    }

    public void setRestriction(String restriction) {
        this.restriction = restriction;
    }

    public umm_BDT getUmm_bdt() {
        return umm_bdt;
    }

    public void setUmm_bdt(umm_BDT umm_bdt) {
        this.umm_bdt = umm_bdt;
    }

}






import java.util.List;
import java.util.ArrayList;

public class eTJ_ExtendedTaskAttribute  {

    private String value;





    private eTJ_Extend etj_extend;


    public eTJ_ExtendedTaskAttribute(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public eTJ_Extend getEtj_extend() {
        return etj_extend;
    }

    public void setEtj_extend(eTJ_Extend etj_extend) {
        this.etj_extend = etj_extend;
    }

}
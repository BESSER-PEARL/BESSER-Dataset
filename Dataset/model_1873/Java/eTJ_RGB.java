





import java.util.List;
import java.util.ArrayList;

public class eTJ_RGB  {

    private String value;





    private eTJ_CellColor etj_cellcolor;


    public eTJ_RGB(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public eTJ_CellColor getEtj_cellcolor() {
        return etj_cellcolor;
    }

    public void setEtj_cellcolor(eTJ_CellColor etj_cellcolor) {
        this.etj_cellcolor = etj_cellcolor;
    }

}






import java.util.List;
import java.util.ArrayList;

public class eTJ_Criterion  {

    private String direction;
    private String columnId;





    private eTJ_Sort etj_sort;


    public eTJ_Criterion(
        String direction,        String columnId    ) {
        this.direction = direction;
        this.columnId = columnId;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getColumnid() {
        return columnId;
    }

    public void setColumnid(String columnId) {
        this.columnId = columnId;
    }

    public eTJ_Sort getEtj_sort() {
        return etj_sort;
    }

    public void setEtj_sort(eTJ_Sort etj_sort) {
        this.etj_sort = etj_sort;
    }

}






import java.util.List;
import java.util.ArrayList;

public class metrics_Mapping extends Base {

    private String firstDataRow;
    private String headerRow;
    private String intervalHint;



    public metrics_Mapping(
        String firstDataRow,        String headerRow,        String intervalHint    ) {
        super(
        );
        this.firstDataRow = firstDataRow;
        this.headerRow = headerRow;
        this.intervalHint = intervalHint;
    }


    public String getFirstdatarow() {
        return firstDataRow;
    }

    public void setFirstdatarow(String firstDataRow) {
        this.firstDataRow = firstDataRow;
    }
    public String getHeaderrow() {
        return headerRow;
    }

    public void setHeaderrow(String headerRow) {
        this.headerRow = headerRow;
    }
    public String getIntervalhint() {
        return intervalHint;
    }

    public void setIntervalhint(String intervalHint) {
        this.intervalHint = intervalHint;
    }


}






import java.util.List;
import java.util.ArrayList;

public class metrics_Mapping extends Base {

    private String headerRow;
    private String firstDataRow;
    private String intervalHint;



    public metrics_Mapping(
        String headerRow,        String firstDataRow,        String intervalHint    ) {
        super(
        );
        this.headerRow = headerRow;
        this.firstDataRow = firstDataRow;
        this.intervalHint = intervalHint;
    }


    public String getHeaderrow() {
        return headerRow;
    }

    public void setHeaderrow(String headerRow) {
        this.headerRow = headerRow;
    }
    public String getFirstdatarow() {
        return firstDataRow;
    }

    public void setFirstdatarow(String firstDataRow) {
        this.firstDataRow = firstDataRow;
    }
    public String getIntervalhint() {
        return intervalHint;
    }

    public void setIntervalhint(String intervalHint) {
        this.intervalHint = intervalHint;
    }


}
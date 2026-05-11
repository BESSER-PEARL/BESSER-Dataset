





import java.util.List;
import java.util.ArrayList;

public class metrics_Mapping extends Base {

    private String intervalHint;
    private String headerRow;
    private String firstDataRow;



    public metrics_Mapping(
        String intervalHint,        String headerRow,        String firstDataRow    ) {
        super(
        );
        this.intervalHint = intervalHint;
        this.headerRow = headerRow;
        this.firstDataRow = firstDataRow;
    }


    public String getIntervalhint() {
        return intervalHint;
    }

    public void setIntervalhint(String intervalHint) {
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


}






import java.util.List;
import java.util.ArrayList;

public class metrics_Mapping extends Base {

    private String firstDataRow;
    private String intervalHint;
    private String headerRow;



    public metrics_Mapping(
        String firstDataRow,        String intervalHint,        String headerRow    ) {
        super(
        );
        this.firstDataRow = firstDataRow;
        this.intervalHint = intervalHint;
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
    public String getHeaderrow() {
        return headerRow;
    }

    public void setHeaderrow(String headerRow) {
        this.headerRow = headerRow;
    }


}
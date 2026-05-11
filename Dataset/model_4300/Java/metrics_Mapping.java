





import java.util.List;
import java.util.ArrayList;

public class metrics_Mapping extends Base {

    private String intervalHint;
    private String firstDataRow;
    private String headerRow;



    public metrics_Mapping(
        String intervalHint,        String firstDataRow,        String headerRow    ) {
        super(
        );
        this.intervalHint = intervalHint;
        this.firstDataRow = firstDataRow;
        this.headerRow = headerRow;
    }


    public String getIntervalhint() {
        return intervalHint;
    }

    public void setIntervalhint(String intervalHint) {
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


}
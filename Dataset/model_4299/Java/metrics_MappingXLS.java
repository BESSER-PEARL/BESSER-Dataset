





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingXLS extends Mapping {

    private String sheetNumber;
    private String headerRow;
    private String firstDataRow;



    public metrics_MappingXLS(
        String sheetNumber,        String headerRow,        String firstDataRow    ) {
        super(
        );
        this.sheetNumber = sheetNumber;
        this.headerRow = headerRow;
        this.firstDataRow = firstDataRow;
    }


    public String getSheetnumber() {
        return sheetNumber;
    }

    public void setSheetnumber(String sheetNumber) {
        this.sheetNumber = sheetNumber;
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
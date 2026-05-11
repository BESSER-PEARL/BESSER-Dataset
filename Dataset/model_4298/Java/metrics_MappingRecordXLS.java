





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingRecordXLS extends MappingRecord {

    private String column;
    private String row;



    public metrics_MappingRecordXLS(
        String column,        String row    ) {
        super(
        );
        this.column = column;
        this.row = row;
    }


    public String getColumn() {
        return column;
    }

    public void setColumn(String column) {
        this.column = column;
    }
    public String getRow() {
        return row;
    }

    public void setRow(String row) {
        this.row = row;
    }


}






import java.util.List;
import java.util.ArrayList;

public class nosql_Cell  {

    private String value;





    private nosql_Row nosql_row;




    private nosql_Column nosql_column;


    public nosql_Cell(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public nosql_Row getNosql_row() {
        return nosql_row;
    }

    public void setNosql_row(nosql_Row nosql_row) {
        this.nosql_row = nosql_row;
    }
    public nosql_Column getNosql_column() {
        return nosql_column;
    }

    public void setNosql_column(nosql_Column nosql_column) {
        this.nosql_column = nosql_column;
    }

}
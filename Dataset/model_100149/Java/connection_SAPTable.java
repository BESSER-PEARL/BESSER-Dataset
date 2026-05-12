





import java.util.List;
import java.util.ArrayList;

public class connection_SAPTable extends MetadataTable {

    private String tableSearchType;



    public connection_SAPTable(
        String tableSearchType    ) {
        super(
        );
        this.tableSearchType = tableSearchType;
    }


    public String getTablesearchtype() {
        return tableSearchType;
    }

    public void setTablesearchtype(String tableSearchType) {
        this.tableSearchType = tableSearchType;
    }


}
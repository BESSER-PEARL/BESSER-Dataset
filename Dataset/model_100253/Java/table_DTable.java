





import java.util.List;
import java.util.ArrayList;

public class table_DTable extends LineContainer, DRepresentation {

    private int headerColumnWidth;



    public table_DTable(
        int headerColumnWidth    ) {
        super(
        );
        this.headerColumnWidth = headerColumnWidth;
    }


    public int getHeadercolumnwidth() {
        return headerColumnWidth;
    }

    public void setHeadercolumnwidth(int headerColumnWidth) {
        this.headerColumnWidth = headerColumnWidth;
    }


}
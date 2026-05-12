





import java.util.List;
import java.util.ArrayList;

public class table_DTable extends DRepresentation, LineContainer, DTableElementUpdater {

    private int headerColumnWidth;





    private List<table_DColumn> table_dcolumns;




    private table_DColumn table_dcolumn;


    public table_DTable(
        int headerColumnWidth    ) {
        super(
        );
        this.headerColumnWidth = headerColumnWidth;
        this.table_dcolumns = new ArrayList<>();
    }

    public table_DTable(
        int headerColumnWidth        ArrayList<table_DColumn> table_dcolumns    ) {
        this.headerColumnWidth = headerColumnWidth;
        this.table_dcolumns = table_dcolumns;
    }

    public int getHeadercolumnwidth() {
        return headerColumnWidth;
    }

    public void setHeadercolumnwidth(int headerColumnWidth) {
        this.headerColumnWidth = headerColumnWidth;
    }

    public List<table_DColumn> getTable_dcolumns() {
        return table_dcolumns;
    }

    public void addTable_dcolumn(Table_dcolumn table_dcolumn) {
        this.table_dcolumns.add(table_dcolumn);
    }
    public table_DColumn getTable_dcolumn() {
        return table_dcolumn;
    }

    public void setTable_dcolumn(table_DColumn table_dcolumn) {
        this.table_dcolumn = table_dcolumn;
    }

}
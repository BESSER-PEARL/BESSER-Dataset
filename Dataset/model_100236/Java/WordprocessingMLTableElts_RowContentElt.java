





import java.util.List;
import java.util.ArrayList;

public class WordprocessingMLTableElts_RowContentElt  {






    private List<TableCellElt> tablecellelts;




    private RunLevelElt runlevelelt;




    private RowElt rowelt;


    public WordprocessingMLTableElts_RowContentElt(
    ) {
        this.tablecellelts = new ArrayList<>();
    }

    public WordprocessingMLTableElts_RowContentElt(
        ArrayList<TableCellElt> tablecellelts    ) {
        this.tablecellelts = tablecellelts;
    }


    public List<TableCellElt> getTablecellelts() {
        return tablecellelts;
    }

    public void addTablecellelt(Tablecellelt tablecellelt) {
        this.tablecellelts.add(tablecellelt);
    }
    public RunLevelElt getRunlevelelt() {
        return runlevelelt;
    }

    public void setRunlevelelt(RunLevelElt runlevelelt) {
        this.runlevelelt = runlevelelt;
    }
    public RowElt getRowelt() {
        return rowelt;
    }

    public void setRowelt(RowElt rowelt) {
        this.rowelt = rowelt;
    }

}
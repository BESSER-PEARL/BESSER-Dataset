





import java.util.List;
import java.util.ArrayList;

public class WordprocessingMLStyles_RowContentElt  {






    private RunLevelElt runlevelelt;




    private List<TableCellElt> tablecellelts;




    private RowElt rowelt;


    public WordprocessingMLStyles_RowContentElt(
    ) {
        this.tablecellelts = new ArrayList<>();
    }

    public WordprocessingMLStyles_RowContentElt(
        ArrayList<TableCellElt> tablecellelts    ) {
        this.tablecellelts = tablecellelts;
    }


    public RunLevelElt getRunlevelelt() {
        return runlevelelt;
    }

    public void setRunlevelelt(RunLevelElt runlevelelt) {
        this.runlevelelt = runlevelelt;
    }
    public List<TableCellElt> getTablecellelts() {
        return tablecellelts;
    }

    public void addTablecellelt(Tablecellelt tablecellelt) {
        this.tablecellelts.add(tablecellelt);
    }
    public RowElt getRowelt() {
        return rowelt;
    }

    public void setRowelt(RowElt rowelt) {
        this.rowelt = rowelt;
    }

}
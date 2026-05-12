





import java.util.List;
import java.util.ArrayList;

public class WordprocessingMLTableElts_TableCellElt  {






    private List<BlockLevelElt> blocklevelelts;




    private RowContentElt rowcontentelt;




    private TableCellPrElt tablecellprelt;


    public WordprocessingMLTableElts_TableCellElt(
    ) {
        this.blocklevelelts = new ArrayList<>();
    }

    public WordprocessingMLTableElts_TableCellElt(
        ArrayList<BlockLevelElt> blocklevelelts    ) {
        this.blocklevelelts = blocklevelelts;
    }


    public List<BlockLevelElt> getBlocklevelelts() {
        return blocklevelelts;
    }

    public void addBlocklevelelt(Blocklevelelt blocklevelelt) {
        this.blocklevelelts.add(blocklevelelt);
    }
    public RowContentElt getRowcontentelt() {
        return rowcontentelt;
    }

    public void setRowcontentelt(RowContentElt rowcontentelt) {
        this.rowcontentelt = rowcontentelt;
    }
    public TableCellPrElt getTablecellprelt() {
        return tablecellprelt;
    }

    public void setTablecellprelt(TableCellPrElt tablecellprelt) {
        this.tablecellprelt = tablecellprelt;
    }

}
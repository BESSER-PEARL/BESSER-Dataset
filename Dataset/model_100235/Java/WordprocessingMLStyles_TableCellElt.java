





import java.util.List;
import java.util.ArrayList;

public class WordprocessingMLStyles_TableCellElt  {






    private List<BlockLevelElt> blocklevelelts;




    private RowContentElt rowcontentelt;


    public WordprocessingMLStyles_TableCellElt(
    ) {
        this.blocklevelelts = new ArrayList<>();
    }

    public WordprocessingMLStyles_TableCellElt(
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

}
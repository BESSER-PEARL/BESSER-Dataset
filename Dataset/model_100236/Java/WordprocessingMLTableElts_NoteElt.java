





import java.util.List;
import java.util.ArrayList;

public class WordprocessingMLTableElts_NoteElt  {

    private None type;
    private None suppressRef;





    private List<BlockLevelElt> blocklevelelts;


    public WordprocessingMLTableElts_NoteElt(
        None type,        None suppressRef    ) {
        this.type = type;
        this.suppressRef = suppressRef;
        this.blocklevelelts = new ArrayList<>();
    }

    public WordprocessingMLTableElts_NoteElt(
        None type,        None suppressRef        ArrayList<BlockLevelElt> blocklevelelts    ) {
        this.type = type;
        this.suppressRef = suppressRef;
        this.blocklevelelts = blocklevelelts;
    }

    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public None getSuppressref() {
        return suppressRef;
    }

    public void setSuppressref(None suppressRef) {
        this.suppressRef = suppressRef;
    }

    public List<BlockLevelElt> getBlocklevelelts() {
        return blocklevelelts;
    }

    public void addBlocklevelelt(Blocklevelelt blocklevelelt) {
        this.blocklevelelts.add(blocklevelelt);
    }

}
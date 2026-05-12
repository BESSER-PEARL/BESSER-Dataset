





import java.util.List;
import java.util.ArrayList;

public class WordprocessingMLBasicDef_BodyElt  {






    private WordDocument worddocument;




    private SectPrElt sectprelt;




    private List<BlockLevelElt> blocklevelelts;


    public WordprocessingMLBasicDef_BodyElt(
    ) {
        this.blocklevelelts = new ArrayList<>();
    }

    public WordprocessingMLBasicDef_BodyElt(
        ArrayList<BlockLevelElt> blocklevelelts    ) {
        this.blocklevelelts = blocklevelelts;
    }


    public WordDocument getWorddocument() {
        return worddocument;
    }

    public void setWorddocument(WordDocument worddocument) {
        this.worddocument = worddocument;
    }
    public SectPrElt getSectprelt() {
        return sectprelt;
    }

    public void setSectprelt(SectPrElt sectprelt) {
        this.sectprelt = sectprelt;
    }
    public List<BlockLevelElt> getBlocklevelelts() {
        return blocklevelelts;
    }

    public void addBlocklevelelt(Blocklevelelt blocklevelelt) {
        this.blocklevelelts.add(blocklevelelt);
    }

}
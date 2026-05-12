





import java.util.List;
import java.util.ArrayList;

public class WordprocessingMLBasicDef_ParaElt extends BlockLevelChunkElt {






    private List<ParaContentElt> paracontentelts;


    public WordprocessingMLBasicDef_ParaElt(
    ) {
        super(
        );
        this.paracontentelts = new ArrayList<>();
    }

    public WordprocessingMLBasicDef_ParaElt(
        ArrayList<ParaContentElt> paracontentelts    ) {
        this.paracontentelts = paracontentelts;
    }


    public List<ParaContentElt> getParacontentelts() {
        return paracontentelts;
    }

    public void addParacontentelt(Paracontentelt paracontentelt) {
        this.paracontentelts.add(paracontentelt);
    }

}
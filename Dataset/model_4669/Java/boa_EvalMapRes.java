





import java.util.List;
import java.util.ArrayList;

public class boa_EvalMapRes extends EvalRes {






    private List<boa_StringToEvalResMap> boa_stringtoevalresmaps;


    public boa_EvalMapRes(
    ) {
        super(
        );
        this.boa_stringtoevalresmaps = new ArrayList<>();
    }

    public boa_EvalMapRes(
        ArrayList<boa_StringToEvalResMap> boa_stringtoevalresmaps    ) {
        this.boa_stringtoevalresmaps = boa_stringtoevalresmaps;
    }


    public List<boa_StringToEvalResMap> getBoa_stringtoevalresmaps() {
        return boa_stringtoevalresmaps;
    }

    public void addBoa_stringtoevalresmap(Boa_stringtoevalresmap boa_stringtoevalresmap) {
        this.boa_stringtoevalresmaps.add(boa_stringtoevalresmap);
    }

}
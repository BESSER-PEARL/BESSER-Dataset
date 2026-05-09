





import java.util.List;
import java.util.ArrayList;

public class minioclcs_ExpCS extends CSTrace {






    private minioclcs_LetVarCS minioclcs_letvarcs;




    private minioclcs_InvariantCS minioclcs_invariantcs;




    private minioclcs_RoundedBracketClauseCS minioclcs_roundedbracketclausecs;


    public minioclcs_ExpCS(
    ) {
        super(
        );
    }



    public minioclcs_LetVarCS getMinioclcs_letvarcs() {
        return minioclcs_letvarcs;
    }

    public void setMinioclcs_letvarcs(minioclcs_LetVarCS minioclcs_letvarcs) {
        this.minioclcs_letvarcs = minioclcs_letvarcs;
    }
    public minioclcs_InvariantCS getMinioclcs_invariantcs() {
        return minioclcs_invariantcs;
    }

    public void setMinioclcs_invariantcs(minioclcs_InvariantCS minioclcs_invariantcs) {
        this.minioclcs_invariantcs = minioclcs_invariantcs;
    }
    public minioclcs_RoundedBracketClauseCS getMinioclcs_roundedbracketclausecs() {
        return minioclcs_roundedbracketclausecs;
    }

    public void setMinioclcs_roundedbracketclausecs(minioclcs_RoundedBracketClauseCS minioclcs_roundedbracketclausecs) {
        this.minioclcs_roundedbracketclausecs = minioclcs_roundedbracketclausecs;
    }

}
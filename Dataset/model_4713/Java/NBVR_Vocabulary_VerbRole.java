





import java.util.List;
import java.util.ArrayList;

public class NBVR_Vocabulary_VerbRole  {

    private boolean isRange;





    private Term term;


    public NBVR_Vocabulary_VerbRole(
        boolean isRange    ) {
        this.isRange = isRange;
    }


    public boolean getIsrange() {
        return isRange;
    }

    public void setIsrange(boolean isRange) {
        this.isRange = isRange;
    }

    public Term getTerm() {
        return term;
    }

    public void setTerm(Term term) {
        this.term = term;
    }

}
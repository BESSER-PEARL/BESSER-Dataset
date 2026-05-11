





import java.util.List;
import java.util.ArrayList;

public class NBVR_Vocabulary_VocVerb extends VocabularyItem {

    private int arity;



    public NBVR_Vocabulary_VocVerb(
        int arity    ) {
        super(
        );
        this.arity = arity;
    }


    public int getArity() {
        return arity;
    }

    public void setArity(int arity) {
        this.arity = arity;
    }


}






import java.util.List;
import java.util.ArrayList;

public class NBVR_Vocabulary_VocNoun extends VocabularyItem {

    private boolean massNoun;



    public NBVR_Vocabulary_VocNoun(
        boolean massNoun    ) {
        super(
        );
        this.massNoun = massNoun;
    }


    public boolean getMassnoun() {
        return massNoun;
    }

    public void setMassnoun(boolean massNoun) {
        this.massNoun = massNoun;
    }


}
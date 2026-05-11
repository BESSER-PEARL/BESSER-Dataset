





import java.util.List;
import java.util.ArrayList;

public class NBVR_Grammar_VerbPhrase  {

    private String modality;
    private boolean negated;



    public NBVR_Grammar_VerbPhrase(
        String modality,        boolean negated    ) {
        this.modality = modality;
        this.negated = negated;
    }


    public String getModality() {
        return modality;
    }

    public void setModality(String modality) {
        this.modality = modality;
    }
    public boolean getNegated() {
        return negated;
    }

    public void setNegated(boolean negated) {
        this.negated = negated;
    }


}
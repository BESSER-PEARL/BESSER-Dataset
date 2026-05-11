





import java.util.List;
import java.util.ArrayList;

public class alf_Multiplicity  {

    private boolean nonUnique;
    private boolean sequence;
    private boolean ordered;





    private alf_TypePart alf_typepart;


    public alf_Multiplicity(
        boolean nonUnique,        boolean sequence,        boolean ordered    ) {
        this.nonUnique = nonUnique;
        this.sequence = sequence;
        this.ordered = ordered;
    }


    public boolean getNonunique() {
        return nonUnique;
    }

    public void setNonunique(boolean nonUnique) {
        this.nonUnique = nonUnique;
    }
    public boolean getSequence() {
        return sequence;
    }

    public void setSequence(boolean sequence) {
        this.sequence = sequence;
    }
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }

    public alf_TypePart getAlf_typepart() {
        return alf_typepart;
    }

    public void setAlf_typepart(alf_TypePart alf_typepart) {
        this.alf_typepart = alf_typepart;
    }

}
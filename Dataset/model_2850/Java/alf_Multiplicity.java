





import java.util.List;
import java.util.ArrayList;

public class alf_Multiplicity  {

    private boolean isNonUnique;
    private boolean isOrdered;
    private boolean isSequence;





    private alf_TypePart alf_typepart;


    public alf_Multiplicity(
        boolean isNonUnique,        boolean isOrdered,        boolean isSequence    ) {
        this.isNonUnique = isNonUnique;
        this.isOrdered = isOrdered;
        this.isSequence = isSequence;
    }


    public boolean getIsnonunique() {
        return isNonUnique;
    }

    public void setIsnonunique(boolean isNonUnique) {
        this.isNonUnique = isNonUnique;
    }
    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }
    public boolean getIssequence() {
        return isSequence;
    }

    public void setIssequence(boolean isSequence) {
        this.isSequence = isSequence;
    }

    public alf_TypePart getAlf_typepart() {
        return alf_typepart;
    }

    public void setAlf_typepart(alf_TypePart alf_typepart) {
        this.alf_typepart = alf_typepart;
    }

}
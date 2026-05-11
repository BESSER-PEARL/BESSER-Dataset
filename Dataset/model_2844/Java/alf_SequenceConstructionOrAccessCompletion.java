





import java.util.List;
import java.util.ArrayList;

public class alf_SequenceConstructionOrAccessCompletion  {

    private boolean multiplicityIndicator;





    private alf_AccessCompletion alf_accesscompletion;




    private alf_SequenceConstructionExpression alf_sequenceconstructionexpression;




    private alf_NameExpression alf_nameexpression;




    private alf_PartialSequenceConstructionCompletion alf_partialsequenceconstructioncompletion;


    public alf_SequenceConstructionOrAccessCompletion(
        boolean multiplicityIndicator    ) {
        this.multiplicityIndicator = multiplicityIndicator;
    }


    public boolean getMultiplicityindicator() {
        return multiplicityIndicator;
    }

    public void setMultiplicityindicator(boolean multiplicityIndicator) {
        this.multiplicityIndicator = multiplicityIndicator;
    }

    public alf_AccessCompletion getAlf_accesscompletion() {
        return alf_accesscompletion;
    }

    public void setAlf_accesscompletion(alf_AccessCompletion alf_accesscompletion) {
        this.alf_accesscompletion = alf_accesscompletion;
    }
    public alf_SequenceConstructionExpression getAlf_sequenceconstructionexpression() {
        return alf_sequenceconstructionexpression;
    }

    public void setAlf_sequenceconstructionexpression(alf_SequenceConstructionExpression alf_sequenceconstructionexpression) {
        this.alf_sequenceconstructionexpression = alf_sequenceconstructionexpression;
    }
    public alf_NameExpression getAlf_nameexpression() {
        return alf_nameexpression;
    }

    public void setAlf_nameexpression(alf_NameExpression alf_nameexpression) {
        this.alf_nameexpression = alf_nameexpression;
    }
    public alf_PartialSequenceConstructionCompletion getAlf_partialsequenceconstructioncompletion() {
        return alf_partialsequenceconstructioncompletion;
    }

    public void setAlf_partialsequenceconstructioncompletion(alf_PartialSequenceConstructionCompletion alf_partialsequenceconstructioncompletion) {
        this.alf_partialsequenceconstructioncompletion = alf_partialsequenceconstructioncompletion;
    }

}
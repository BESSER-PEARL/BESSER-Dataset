





import java.util.List;
import java.util.ArrayList;

public class alf_SequenceConstructionCompletion  {

    private boolean multiplicityIndicator;





    private alf_SequenceConstructionExpression alf_sequenceconstructionexpression;




    private alf_InstanceCreationExpression alf_instancecreationexpression;


    public alf_SequenceConstructionCompletion(
        boolean multiplicityIndicator    ) {
        this.multiplicityIndicator = multiplicityIndicator;
    }


    public boolean getMultiplicityindicator() {
        return multiplicityIndicator;
    }

    public void setMultiplicityindicator(boolean multiplicityIndicator) {
        this.multiplicityIndicator = multiplicityIndicator;
    }

    public alf_SequenceConstructionExpression getAlf_sequenceconstructionexpression() {
        return alf_sequenceconstructionexpression;
    }

    public void setAlf_sequenceconstructionexpression(alf_SequenceConstructionExpression alf_sequenceconstructionexpression) {
        this.alf_sequenceconstructionexpression = alf_sequenceconstructionexpression;
    }
    public alf_InstanceCreationExpression getAlf_instancecreationexpression() {
        return alf_instancecreationexpression;
    }

    public void setAlf_instancecreationexpression(alf_InstanceCreationExpression alf_instancecreationexpression) {
        this.alf_instancecreationexpression = alf_instancecreationexpression;
    }

}
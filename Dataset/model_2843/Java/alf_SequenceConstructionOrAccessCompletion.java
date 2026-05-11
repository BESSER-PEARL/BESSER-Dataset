





import java.util.List;
import java.util.ArrayList;

public class alf_SequenceConstructionOrAccessCompletion  {

    private boolean multiplicityIndicator;





    private alf_NameExpression alf_nameexpression;


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

    public alf_NameExpression getAlf_nameexpression() {
        return alf_nameexpression;
    }

    public void setAlf_nameexpression(alf_NameExpression alf_nameexpression) {
        this.alf_nameexpression = alf_nameexpression;
    }

}
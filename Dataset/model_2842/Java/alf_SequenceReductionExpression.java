





import java.util.List;
import java.util.ArrayList;

public class alf_SequenceReductionExpression extends SuffixExpression {

    private boolean isOrdered;





    private alf_QualifiedNameWithBinding alf_qualifiednamewithbinding;




    private alf_SuffixExpression alf_suffixexpression;


    public alf_SequenceReductionExpression(
        boolean isOrdered    ) {
        super(
        );
        this.isOrdered = isOrdered;
    }


    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }

    public alf_QualifiedNameWithBinding getAlf_qualifiednamewithbinding() {
        return alf_qualifiednamewithbinding;
    }

    public void setAlf_qualifiednamewithbinding(alf_QualifiedNameWithBinding alf_qualifiednamewithbinding) {
        this.alf_qualifiednamewithbinding = alf_qualifiednamewithbinding;
    }
    public alf_SuffixExpression getAlf_suffixexpression() {
        return alf_suffixexpression;
    }

    public void setAlf_suffixexpression(alf_SuffixExpression alf_suffixexpression) {
        this.alf_suffixexpression = alf_suffixexpression;
    }

}
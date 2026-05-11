





import java.util.List;
import java.util.ArrayList;

public class alf_SequenceOperationExpression extends SuffixExpression {






    private alf_SuffixExpression alf_suffixexpression;




    private alf_QualifiedNameWithBinding alf_qualifiednamewithbinding;




    private alf_Tuple alf_tuple;


    public alf_SequenceOperationExpression(
    ) {
        super(
        );
    }



    public alf_SuffixExpression getAlf_suffixexpression() {
        return alf_suffixexpression;
    }

    public void setAlf_suffixexpression(alf_SuffixExpression alf_suffixexpression) {
        this.alf_suffixexpression = alf_suffixexpression;
    }
    public alf_QualifiedNameWithBinding getAlf_qualifiednamewithbinding() {
        return alf_qualifiednamewithbinding;
    }

    public void setAlf_qualifiednamewithbinding(alf_QualifiedNameWithBinding alf_qualifiednamewithbinding) {
        this.alf_qualifiednamewithbinding = alf_qualifiednamewithbinding;
    }
    public alf_Tuple getAlf_tuple() {
        return alf_tuple;
    }

    public void setAlf_tuple(alf_Tuple alf_tuple) {
        this.alf_tuple = alf_tuple;
    }

}
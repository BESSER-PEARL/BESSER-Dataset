





import java.util.List;
import java.util.ArrayList;

public class alf_Expression extends InitializationExpression {






    private alf_ParenthesizedExpression alf_parenthesizedexpression;




    private alf_SequenceOperationOrReductionOrExpansion alf_sequenceoperationorreductionorexpansion;


    public alf_Expression(
    ) {
        super(
        );
    }



    public alf_ParenthesizedExpression getAlf_parenthesizedexpression() {
        return alf_parenthesizedexpression;
    }

    public void setAlf_parenthesizedexpression(alf_ParenthesizedExpression alf_parenthesizedexpression) {
        this.alf_parenthesizedexpression = alf_parenthesizedexpression;
    }
    public alf_SequenceOperationOrReductionOrExpansion getAlf_sequenceoperationorreductionorexpansion() {
        return alf_sequenceoperationorreductionorexpansion;
    }

    public void setAlf_sequenceoperationorreductionorexpansion(alf_SequenceOperationOrReductionOrExpansion alf_sequenceoperationorreductionorexpansion) {
        this.alf_sequenceoperationorreductionorexpansion = alf_sequenceoperationorreductionorexpansion;
    }

}
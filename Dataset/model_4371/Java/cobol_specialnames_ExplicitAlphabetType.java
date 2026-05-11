





import java.util.List;
import java.util.ArrayList;

public class cobol_specialnames_ExplicitAlphabetType extends AlphabetType {






    private List<RangeExpression> rangeexpressions;


    public cobol_specialnames_ExplicitAlphabetType(
    ) {
        super(
        );
        this.rangeexpressions = new ArrayList<>();
    }

    public cobol_specialnames_ExplicitAlphabetType(
        ArrayList<RangeExpression> rangeexpressions    ) {
        this.rangeexpressions = rangeexpressions;
    }


    public List<RangeExpression> getRangeexpressions() {
        return rangeexpressions;
    }

    public void addRangeexpression(Rangeexpression rangeexpression) {
        this.rangeexpressions.add(rangeexpression);
    }

}
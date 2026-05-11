





import java.util.List;
import java.util.ArrayList;

public class cobol_arithmetics_RangeExpression extends ArithmeticExpression {






    private Through through;




    private List<RangeExpressionChild> rangeexpressionchilds;


    public cobol_arithmetics_RangeExpression(
    ) {
        super(
        );
        this.rangeexpressionchilds = new ArrayList<>();
    }

    public cobol_arithmetics_RangeExpression(
        ArrayList<RangeExpressionChild> rangeexpressionchilds    ) {
        this.rangeexpressionchilds = rangeexpressionchilds;
    }


    public Through getThrough() {
        return through;
    }

    public void setThrough(Through through) {
        this.through = through;
    }
    public List<RangeExpressionChild> getRangeexpressionchilds() {
        return rangeexpressionchilds;
    }

    public void addRangeexpressionchild(Rangeexpressionchild rangeexpressionchild) {
        this.rangeexpressionchilds.add(rangeexpressionchild);
    }

}
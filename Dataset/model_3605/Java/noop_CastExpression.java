





import java.util.List;
import java.util.ArrayList;

public class noop_CastExpression extends Expression {






    private List<noop_Index> noop_indexs;




    private noop_Expression noop_expression;




    private noop_NoopClass noop_noopclass;


    public noop_CastExpression(
    ) {
        super(
        );
        this.noop_indexs = new ArrayList<>();
    }

    public noop_CastExpression(
        ArrayList<noop_Index> noop_indexs    ) {
        this.noop_indexs = noop_indexs;
    }


    public List<noop_Index> getNoop_indexs() {
        return noop_indexs;
    }

    public void addNoop_index(Noop_index noop_index) {
        this.noop_indexs.add(noop_index);
    }
    public noop_Expression getNoop_expression() {
        return noop_expression;
    }

    public void setNoop_expression(noop_Expression noop_expression) {
        this.noop_expression = noop_expression;
    }
    public noop_NoopClass getNoop_noopclass() {
        return noop_noopclass;
    }

    public void setNoop_noopclass(noop_NoopClass noop_noopclass) {
        this.noop_noopclass = noop_noopclass;
    }

}
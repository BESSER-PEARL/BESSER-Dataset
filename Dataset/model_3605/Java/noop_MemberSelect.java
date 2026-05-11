





import java.util.List;
import java.util.ArrayList;

public class noop_MemberSelect extends Expression {

    private boolean hasArgs;





    private List<noop_Index> noop_indexs;




    private noop_Member noop_member;




    private List<noop_Expression> noop_expressions;




    private noop_Expression noop_expression;


    public noop_MemberSelect(
        boolean hasArgs    ) {
        super(
        );
        this.hasArgs = hasArgs;
        this.noop_indexs = new ArrayList<>();
        this.noop_expressions = new ArrayList<>();
    }

    public noop_MemberSelect(
        boolean hasArgs        ArrayList<noop_Index> noop_indexs,        ArrayList<noop_Expression> noop_expressions    ) {
        this.hasArgs = hasArgs;
        this.noop_indexs = noop_indexs;
        this.noop_expressions = noop_expressions;
    }

    public boolean getHasargs() {
        return hasArgs;
    }

    public void setHasargs(boolean hasArgs) {
        this.hasArgs = hasArgs;
    }

    public List<noop_Index> getNoop_indexs() {
        return noop_indexs;
    }

    public void addNoop_index(Noop_index noop_index) {
        this.noop_indexs.add(noop_index);
    }
    public noop_Member getNoop_member() {
        return noop_member;
    }

    public void setNoop_member(noop_Member noop_member) {
        this.noop_member = noop_member;
    }
    public List<noop_Expression> getNoop_expressions() {
        return noop_expressions;
    }

    public void addNoop_expression(Noop_expression noop_expression) {
        this.noop_expressions.add(noop_expression);
    }
    public noop_Expression getNoop_expression() {
        return noop_expression;
    }

    public void setNoop_expression(noop_Expression noop_expression) {
        this.noop_expression = noop_expression;
    }

}
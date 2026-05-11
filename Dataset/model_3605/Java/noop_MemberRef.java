





import java.util.List;
import java.util.ArrayList;

public class noop_MemberRef extends Expression {

    private boolean hasArgs;





    private List<noop_Expression> noop_expressions;




    private List<noop_Index> noop_indexs;




    private noop_Member noop_member;


    public noop_MemberRef(
        boolean hasArgs    ) {
        super(
        );
        this.hasArgs = hasArgs;
        this.noop_expressions = new ArrayList<>();
        this.noop_indexs = new ArrayList<>();
    }

    public noop_MemberRef(
        boolean hasArgs        ArrayList<noop_Expression> noop_expressions,        ArrayList<noop_Index> noop_indexs    ) {
        this.hasArgs = hasArgs;
        this.noop_expressions = noop_expressions;
        this.noop_indexs = noop_indexs;
    }

    public boolean getHasargs() {
        return hasArgs;
    }

    public void setHasargs(boolean hasArgs) {
        this.hasArgs = hasArgs;
    }

    public List<noop_Expression> getNoop_expressions() {
        return noop_expressions;
    }

    public void addNoop_expression(Noop_expression noop_expression) {
        this.noop_expressions.add(noop_expression);
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

}
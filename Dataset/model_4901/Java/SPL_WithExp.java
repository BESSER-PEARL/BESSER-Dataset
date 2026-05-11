





import java.util.List;
import java.util.ArrayList;

public class SPL_WithExp extends Expression {






    private List<SPL_MessageField> spl_messagefields;




    private SPL_Expression spl_expression;


    public SPL_WithExp(
    ) {
        super(
        );
        this.spl_messagefields = new ArrayList<>();
    }

    public SPL_WithExp(
        ArrayList<SPL_MessageField> spl_messagefields    ) {
        this.spl_messagefields = spl_messagefields;
    }


    public List<SPL_MessageField> getSpl_messagefields() {
        return spl_messagefields;
    }

    public void addSpl_messagefield(Spl_messagefield spl_messagefield) {
        this.spl_messagefields.add(spl_messagefield);
    }
    public SPL_Expression getSpl_expression() {
        return spl_expression;
    }

    public void setSpl_expression(SPL_Expression spl_expression) {
        this.spl_expression = spl_expression;
    }

}
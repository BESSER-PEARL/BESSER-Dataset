





import java.util.List;
import java.util.ArrayList;

public class drn_Expression  {

    private int repeatCST;





    private drn_Assignement drn_assignement;




    private List<drn_With> drn_withs;




    private drn_Expression drn_expression;


    public drn_Expression(
        int repeatCST    ) {
        this.repeatCST = repeatCST;
        this.drn_withs = new ArrayList<>();
    }

    public drn_Expression(
        int repeatCST        ArrayList<drn_With> drn_withs    ) {
        this.repeatCST = repeatCST;
        this.drn_withs = drn_withs;
    }

    public int getRepeatcst() {
        return repeatCST;
    }

    public void setRepeatcst(int repeatCST) {
        this.repeatCST = repeatCST;
    }

    public drn_Assignement getDrn_assignement() {
        return drn_assignement;
    }

    public void setDrn_assignement(drn_Assignement drn_assignement) {
        this.drn_assignement = drn_assignement;
    }
    public List<drn_With> getDrn_withs() {
        return drn_withs;
    }

    public void addDrn_with(Drn_with drn_with) {
        this.drn_withs.add(drn_with);
    }
    public drn_Expression getDrn_expression() {
        return drn_expression;
    }

    public void setDrn_expression(drn_Expression drn_expression) {
        this.drn_expression = drn_expression;
    }

}
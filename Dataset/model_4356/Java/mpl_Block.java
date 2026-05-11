





import java.util.List;
import java.util.ArrayList;

public class mpl_Block  {






    private mpl_WhileLoop mpl_whileloop;




    private mpl_IfStatement mpl_ifstatement;




    private mpl_IfStatement mpl_ifstatement;




    private List<mpl_Statement> mpl_statements;




    private mpl_ForLoop mpl_forloop;


    public mpl_Block(
    ) {
        this.mpl_statements = new ArrayList<>();
    }

    public mpl_Block(
        ArrayList<mpl_Statement> mpl_statements    ) {
        this.mpl_statements = mpl_statements;
    }


    public mpl_WhileLoop getMpl_whileloop() {
        return mpl_whileloop;
    }

    public void setMpl_whileloop(mpl_WhileLoop mpl_whileloop) {
        this.mpl_whileloop = mpl_whileloop;
    }
    public mpl_IfStatement getMpl_ifstatement() {
        return mpl_ifstatement;
    }

    public void setMpl_ifstatement(mpl_IfStatement mpl_ifstatement) {
        this.mpl_ifstatement = mpl_ifstatement;
    }
    public mpl_IfStatement getMpl_ifstatement() {
        return mpl_ifstatement;
    }

    public void setMpl_ifstatement(mpl_IfStatement mpl_ifstatement) {
        this.mpl_ifstatement = mpl_ifstatement;
    }
    public List<mpl_Statement> getMpl_statements() {
        return mpl_statements;
    }

    public void addMpl_statement(Mpl_statement mpl_statement) {
        this.mpl_statements.add(mpl_statement);
    }
    public mpl_ForLoop getMpl_forloop() {
        return mpl_forloop;
    }

    public void setMpl_forloop(mpl_ForLoop mpl_forloop) {
        this.mpl_forloop = mpl_forloop;
    }

}
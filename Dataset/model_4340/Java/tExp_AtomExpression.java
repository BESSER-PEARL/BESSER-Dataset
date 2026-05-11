





import java.util.List;
import java.util.ArrayList;

public class tExp_AtomExpression extends PrologExpression {

    private String atom;





    private tExp_PrologExpression texp_prologexpression;


    public tExp_AtomExpression(
        String atom    ) {
        super(
        );
        this.atom = atom;
    }


    public String getAtom() {
        return atom;
    }

    public void setAtom(String atom) {
        this.atom = atom;
    }

    public tExp_PrologExpression getTexp_prologexpression() {
        return texp_prologexpression;
    }

    public void setTexp_prologexpression(tExp_PrologExpression texp_prologexpression) {
        this.texp_prologexpression = texp_prologexpression;
    }

}
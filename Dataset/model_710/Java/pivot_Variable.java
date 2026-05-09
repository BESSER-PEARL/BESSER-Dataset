





import java.util.List;
import java.util.ArrayList;

public class pivot_Variable extends VariableDeclaration {

    private String implicit;





    private pivot_LetExp pivot_letexp;


    public pivot_Variable(
        String implicit    ) {
        super(
        );
        this.implicit = implicit;
    }


    public String getImplicit() {
        return implicit;
    }

    public void setImplicit(String implicit) {
        this.implicit = implicit;
    }

    public pivot_LetExp getPivot_letexp() {
        return pivot_letexp;
    }

    public void setPivot_letexp(pivot_LetExp pivot_letexp) {
        this.pivot_letexp = pivot_letexp;
    }

}
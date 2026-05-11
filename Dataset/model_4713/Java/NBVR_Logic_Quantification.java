





import java.util.List;
import java.util.ArrayList;

public class NBVR_Logic_Quantification extends Proposition {

    private boolean unique;
    private String kind;





    private Variable variable;


    public NBVR_Logic_Quantification(
        boolean unique,        String kind    ) {
        super(
        );
        this.unique = unique;
        this.kind = kind;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }

}
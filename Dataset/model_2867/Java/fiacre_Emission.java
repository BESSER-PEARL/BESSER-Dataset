





import java.util.List;
import java.util.ArrayList;

public class fiacre_Emission extends Communication {






    private List<fiacre_Exp> fiacre_exps;


    public fiacre_Emission(
    ) {
        super(
        );
        this.fiacre_exps = new ArrayList<>();
    }

    public fiacre_Emission(
        ArrayList<fiacre_Exp> fiacre_exps    ) {
        this.fiacre_exps = fiacre_exps;
    }


    public List<fiacre_Exp> getFiacre_exps() {
        return fiacre_exps;
    }

    public void addFiacre_exp(Fiacre_exp fiacre_exp) {
        this.fiacre_exps.add(fiacre_exp);
    }

}
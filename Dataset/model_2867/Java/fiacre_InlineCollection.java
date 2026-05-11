





import java.util.List;
import java.util.ArrayList;

public class fiacre_InlineCollection extends Exp {






    private List<fiacre_Exp> fiacre_exps;


    public fiacre_InlineCollection(
    ) {
        super(
        );
        this.fiacre_exps = new ArrayList<>();
    }

    public fiacre_InlineCollection(
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
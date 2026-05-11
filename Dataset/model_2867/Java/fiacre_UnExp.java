





import java.util.List;
import java.util.ArrayList;

public class fiacre_UnExp extends Exp {

    private String unop;





    private fiacre_Exp fiacre_exp;


    public fiacre_UnExp(
        String unop    ) {
        super(
        );
        this.unop = unop;
    }


    public String getUnop() {
        return unop;
    }

    public void setUnop(String unop) {
        this.unop = unop;
    }

    public fiacre_Exp getFiacre_exp() {
        return fiacre_exp;
    }

    public void setFiacre_exp(fiacre_Exp fiacre_exp) {
        this.fiacre_exp = fiacre_exp;
    }

}
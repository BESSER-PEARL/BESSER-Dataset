





import java.util.List;
import java.util.ArrayList;

public class fiacre_ConstrExp extends Exp {

    private String name;





    private fiacre_Exp fiacre_exp;


    public fiacre_ConstrExp(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fiacre_Exp getFiacre_exp() {
        return fiacre_exp;
    }

    public void setFiacre_exp(fiacre_Exp fiacre_exp) {
        this.fiacre_exp = fiacre_exp;
    }

}
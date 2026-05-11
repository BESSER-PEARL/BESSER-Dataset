





import java.util.List;
import java.util.ArrayList;

public class fiacre_Reception extends Communication {






    private fiacre_Exp fiacre_exp;




    private List<fiacre_Pattern> fiacre_patterns;


    public fiacre_Reception(
    ) {
        super(
        );
        this.fiacre_patterns = new ArrayList<>();
    }

    public fiacre_Reception(
        ArrayList<fiacre_Pattern> fiacre_patterns    ) {
        this.fiacre_patterns = fiacre_patterns;
    }


    public fiacre_Exp getFiacre_exp() {
        return fiacre_exp;
    }

    public void setFiacre_exp(fiacre_Exp fiacre_exp) {
        this.fiacre_exp = fiacre_exp;
    }
    public List<fiacre_Pattern> getFiacre_patterns() {
        return fiacre_patterns;
    }

    public void addFiacre_pattern(Fiacre_pattern fiacre_pattern) {
        this.fiacre_patterns.add(fiacre_pattern);
    }

}
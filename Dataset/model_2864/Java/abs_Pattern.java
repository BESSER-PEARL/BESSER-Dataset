





import java.util.List;
import java.util.ArrayList;

public class abs_Pattern extends Case_branch {






    private abs_Pure_exp abs_pure_exp;




    private List<abs_Pattern> abs_patterns;


    public abs_Pattern(
    ) {
        super(
        );
        this.abs_patterns = new ArrayList<>();
    }

    public abs_Pattern(
        ArrayList<abs_Pattern> abs_patterns    ) {
        this.abs_patterns = abs_patterns;
    }


    public abs_Pure_exp getAbs_pure_exp() {
        return abs_pure_exp;
    }

    public void setAbs_pure_exp(abs_Pure_exp abs_pure_exp) {
        this.abs_pure_exp = abs_pure_exp;
    }
    public List<abs_Pattern> getAbs_patterns() {
        return abs_patterns;
    }

    public void addAbs_pattern(Abs_pattern abs_pattern) {
        this.abs_patterns.add(abs_pattern);
    }

}
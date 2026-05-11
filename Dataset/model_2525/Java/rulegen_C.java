





import java.util.List;
import java.util.ArrayList;

public class rulegen_C  {






    private rulegen_D rulegen_d;




    private rulegen_B rulegen_b;




    private List<rulegen_B> rulegen_bs;




    private rulegen_Context rulegen_context;


    public rulegen_C(
    ) {
        this.rulegen_bs = new ArrayList<>();
    }

    public rulegen_C(
        ArrayList<rulegen_B> rulegen_bs    ) {
        this.rulegen_bs = rulegen_bs;
    }


    public rulegen_D getRulegen_d() {
        return rulegen_d;
    }

    public void setRulegen_d(rulegen_D rulegen_d) {
        this.rulegen_d = rulegen_d;
    }
    public rulegen_B getRulegen_b() {
        return rulegen_b;
    }

    public void setRulegen_b(rulegen_B rulegen_b) {
        this.rulegen_b = rulegen_b;
    }
    public List<rulegen_B> getRulegen_bs() {
        return rulegen_bs;
    }

    public void addRulegen_b(Rulegen_b rulegen_b) {
        this.rulegen_bs.add(rulegen_b);
    }
    public rulegen_Context getRulegen_context() {
        return rulegen_context;
    }

    public void setRulegen_context(rulegen_Context rulegen_context) {
        this.rulegen_context = rulegen_context;
    }

}






import java.util.List;
import java.util.ArrayList;

public class rulegen_B  {






    private rulegen_Context rulegen_context;




    private List<rulegen_A> rulegen_as;




    private rulegen_A rulegen_a;


    public rulegen_B(
    ) {
        this.rulegen_as = new ArrayList<>();
    }

    public rulegen_B(
        ArrayList<rulegen_A> rulegen_as    ) {
        this.rulegen_as = rulegen_as;
    }


    public rulegen_Context getRulegen_context() {
        return rulegen_context;
    }

    public void setRulegen_context(rulegen_Context rulegen_context) {
        this.rulegen_context = rulegen_context;
    }
    public List<rulegen_A> getRulegen_as() {
        return rulegen_as;
    }

    public void addRulegen_a(Rulegen_a rulegen_a) {
        this.rulegen_as.add(rulegen_a);
    }
    public rulegen_A getRulegen_a() {
        return rulegen_a;
    }

    public void setRulegen_a(rulegen_A rulegen_a) {
        this.rulegen_a = rulegen_a;
    }

}
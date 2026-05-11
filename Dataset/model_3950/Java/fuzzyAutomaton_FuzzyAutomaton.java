





import java.util.List;
import java.util.ArrayList;

public class fuzzyAutomaton_FuzzyAutomaton  {

    private String tNorm;
    private String name;



    public fuzzyAutomaton_FuzzyAutomaton(
        String tNorm,        String name    ) {
        this.tNorm = tNorm;
        this.name = name;
    }


    public String getTnorm() {
        return tNorm;
    }

    public void setTnorm(String tNorm) {
        this.tNorm = tNorm;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
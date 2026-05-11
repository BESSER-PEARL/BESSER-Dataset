





import java.util.List;
import java.util.ArrayList;

public class rulegen_Context  {






    private List<rulegen_D> rulegen_ds;


    public rulegen_Context(
    ) {
        this.rulegen_ds = new ArrayList<>();
    }

    public rulegen_Context(
        ArrayList<rulegen_D> rulegen_ds    ) {
        this.rulegen_ds = rulegen_ds;
    }


    public List<rulegen_D> getRulegen_ds() {
        return rulegen_ds;
    }

    public void addRulegen_d(Rulegen_d rulegen_d) {
        this.rulegen_ds.add(rulegen_d);
    }

}
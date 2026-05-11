





import java.util.List;
import java.util.ArrayList;

public class rell_Update extends Relational {






    private List<rell_VariableInit> rell_variableinits;


    public rell_Update(
    ) {
        super(
        );
        this.rell_variableinits = new ArrayList<>();
    }

    public rell_Update(
        ArrayList<rell_VariableInit> rell_variableinits    ) {
        this.rell_variableinits = rell_variableinits;
    }


    public List<rell_VariableInit> getRell_variableinits() {
        return rell_variableinits;
    }

    public void addRell_variableinit(Rell_variableinit rell_variableinit) {
        this.rell_variableinits.add(rell_variableinit);
    }

}
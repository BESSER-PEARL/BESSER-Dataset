





import java.util.List;
import java.util.ArrayList;

public class dfa_Language extends NamedElement {






    private dfa_Dfa dfa_dfa;




    private List<dfa_Symbol> dfa_symbols;


    public dfa_Language(
    ) {
        super(
        );
        this.dfa_symbols = new ArrayList<>();
    }

    public dfa_Language(
        ArrayList<dfa_Symbol> dfa_symbols    ) {
        this.dfa_symbols = dfa_symbols;
    }


    public dfa_Dfa getDfa_dfa() {
        return dfa_dfa;
    }

    public void setDfa_dfa(dfa_Dfa dfa_dfa) {
        this.dfa_dfa = dfa_dfa;
    }
    public List<dfa_Symbol> getDfa_symbols() {
        return dfa_symbols;
    }

    public void addDfa_symbol(Dfa_symbol dfa_symbol) {
        this.dfa_symbols.add(dfa_symbol);
    }

}
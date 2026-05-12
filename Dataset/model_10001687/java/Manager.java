





import java.util.List;
import java.util.ArrayList;

public class Manager  {






    private List<Terminal> terminals;




    private Store store;


    public Manager(
    ) {
        this.terminals = new ArrayList<>();
    }

    public Manager(
        ArrayList<Terminal> terminals    ) {
        this.terminals = terminals;
    }


    public List<Terminal> getTerminals() {
        return terminals;
    }

    public void addTerminal(Terminal terminal) {
        this.terminals.add(terminal);
    }
    public Store getStore() {
        return store;
    }

    public void setStore(Store store) {
        this.store = store;
    }

}
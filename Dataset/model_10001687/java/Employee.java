





import java.util.List;
import java.util.ArrayList;

public class Employee  {






    private Store store;




    private List<Terminal> terminals;


    public Employee(
    ) {
        this.terminals = new ArrayList<>();
    }

    public Employee(
        ArrayList<Terminal> terminals    ) {
        this.terminals = terminals;
    }


    public Store getStore() {
        return store;
    }

    public void setStore(Store store) {
        this.store = store;
    }
    public List<Terminal> getTerminals() {
        return terminals;
    }

    public void addTerminal(Terminal terminal) {
        this.terminals.add(terminal);
    }

}






import java.util.List;
import java.util.ArrayList;

public class cm_seff_Automaton  {






    private List<AbstractAction> abstractactions;


    public cm_seff_Automaton(
    ) {
        this.abstractactions = new ArrayList<>();
    }

    public cm_seff_Automaton(
        ArrayList<AbstractAction> abstractactions    ) {
        this.abstractactions = abstractactions;
    }


    public List<AbstractAction> getAbstractactions() {
        return abstractactions;
    }

    public void addAbstractaction(Abstractaction abstractaction) {
        this.abstractactions.add(abstractaction);
    }

}






import java.util.List;
import java.util.ArrayList;

public class timedAutomata_core_Edge extends core_TAElement, Position {






    private Synchronisation synchronisation;


    public timedAutomata_core_Edge(
    ) {
        super(
        );
    }



    public Synchronisation getSynchronisation() {
        return synchronisation;
    }

    public void setSynchronisation(Synchronisation synchronisation) {
        this.synchronisation = synchronisation;
    }

}
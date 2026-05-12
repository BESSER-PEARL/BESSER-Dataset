





import java.util.List;
import java.util.ArrayList;

public class sml_Parallel extends InteractionFragment {






    private List<sml_Interaction> sml_interactions;


    public sml_Parallel(
    ) {
        super(
        );
        this.sml_interactions = new ArrayList<>();
    }

    public sml_Parallel(
        ArrayList<sml_Interaction> sml_interactions    ) {
        this.sml_interactions = sml_interactions;
    }


    public List<sml_Interaction> getSml_interactions() {
        return sml_interactions;
    }

    public void addSml_interaction(Sml_interaction sml_interaction) {
        this.sml_interactions.add(sml_interaction);
    }

}
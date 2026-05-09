





import java.util.List;
import java.util.ArrayList;

public class shadowrun_Script extends Beschreibbar {






    private List<shadowrun_Placement> shadowrun_placements;




    private shadowrun_PersonaGruppe shadowrun_personagruppe;


    public shadowrun_Script(
    ) {
        super(
        );
        this.shadowrun_placements = new ArrayList<>();
    }

    public shadowrun_Script(
        ArrayList<shadowrun_Placement> shadowrun_placements    ) {
        this.shadowrun_placements = shadowrun_placements;
    }


    public List<shadowrun_Placement> getShadowrun_placements() {
        return shadowrun_placements;
    }

    public void addShadowrun_placement(Shadowrun_placement shadowrun_placement) {
        this.shadowrun_placements.add(shadowrun_placement);
    }
    public shadowrun_PersonaGruppe getShadowrun_personagruppe() {
        return shadowrun_personagruppe;
    }

    public void setShadowrun_personagruppe(shadowrun_PersonaGruppe shadowrun_personagruppe) {
        this.shadowrun_personagruppe = shadowrun_personagruppe;
    }

}
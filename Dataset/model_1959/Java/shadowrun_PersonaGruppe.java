





import java.util.List;
import java.util.ArrayList;

public class shadowrun_PersonaGruppe extends Beschreibbar {






    private List<shadowrun_AbstaktPersona> shadowrun_abstaktpersonas;




    private shadowrun_Placement shadowrun_placement;


    public shadowrun_PersonaGruppe(
    ) {
        super(
        );
        this.shadowrun_abstaktpersonas = new ArrayList<>();
    }

    public shadowrun_PersonaGruppe(
        ArrayList<shadowrun_AbstaktPersona> shadowrun_abstaktpersonas    ) {
        this.shadowrun_abstaktpersonas = shadowrun_abstaktpersonas;
    }


    public List<shadowrun_AbstaktPersona> getShadowrun_abstaktpersonas() {
        return shadowrun_abstaktpersonas;
    }

    public void addShadowrun_abstaktpersona(Shadowrun_abstaktpersona shadowrun_abstaktpersona) {
        this.shadowrun_abstaktpersonas.add(shadowrun_abstaktpersona);
    }
    public shadowrun_Placement getShadowrun_placement() {
        return shadowrun_placement;
    }

    public void setShadowrun_placement(shadowrun_Placement shadowrun_placement) {
        this.shadowrun_placement = shadowrun_placement;
    }

}
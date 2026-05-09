





import java.util.List;
import java.util.ArrayList;

public class essentialoclcs_LetExpCS extends ExpCS {






    private essentialoclcs_LetVariableCS essentialoclcs_letvariablecs;




    private List<essentialoclcs_LetVariableCS> essentialoclcs_letvariablecss;


    public essentialoclcs_LetExpCS(
    ) {
        super(
        );
        this.essentialoclcs_letvariablecss = new ArrayList<>();
    }

    public essentialoclcs_LetExpCS(
        ArrayList<essentialoclcs_LetVariableCS> essentialoclcs_letvariablecss    ) {
        this.essentialoclcs_letvariablecss = essentialoclcs_letvariablecss;
    }


    public essentialoclcs_LetVariableCS getEssentialoclcs_letvariablecs() {
        return essentialoclcs_letvariablecs;
    }

    public void setEssentialoclcs_letvariablecs(essentialoclcs_LetVariableCS essentialoclcs_letvariablecs) {
        this.essentialoclcs_letvariablecs = essentialoclcs_letvariablecs;
    }
    public List<essentialoclcs_LetVariableCS> getEssentialoclcs_letvariablecss() {
        return essentialoclcs_letvariablecss;
    }

    public void addEssentialoclcs_letvariablecs(Essentialoclcs_letvariablecs essentialoclcs_letvariablecs) {
        this.essentialoclcs_letvariablecss.add(essentialoclcs_letvariablecs);
    }

}
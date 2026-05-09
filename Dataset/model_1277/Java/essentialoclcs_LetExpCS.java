





import java.util.List;
import java.util.ArrayList;

public class essentialoclcs_LetExpCS extends ExpCS {

    private boolean isImplicit;





    private List<essentialoclcs_LetVariableCS> essentialoclcs_letvariablecss;




    private essentialoclcs_LetVariableCS essentialoclcs_letvariablecs;


    public essentialoclcs_LetExpCS(
        boolean isImplicit    ) {
        super(
        );
        this.isImplicit = isImplicit;
        this.essentialoclcs_letvariablecss = new ArrayList<>();
    }

    public essentialoclcs_LetExpCS(
        boolean isImplicit        ArrayList<essentialoclcs_LetVariableCS> essentialoclcs_letvariablecss    ) {
        this.isImplicit = isImplicit;
        this.essentialoclcs_letvariablecss = essentialoclcs_letvariablecss;
    }

    public boolean getIsimplicit() {
        return isImplicit;
    }

    public void setIsimplicit(boolean isImplicit) {
        this.isImplicit = isImplicit;
    }

    public List<essentialoclcs_LetVariableCS> getEssentialoclcs_letvariablecss() {
        return essentialoclcs_letvariablecss;
    }

    public void addEssentialoclcs_letvariablecs(Essentialoclcs_letvariablecs essentialoclcs_letvariablecs) {
        this.essentialoclcs_letvariablecss.add(essentialoclcs_letvariablecs);
    }
    public essentialoclcs_LetVariableCS getEssentialoclcs_letvariablecs() {
        return essentialoclcs_letvariablecs;
    }

    public void setEssentialoclcs_letvariablecs(essentialoclcs_LetVariableCS essentialoclcs_letvariablecs) {
        this.essentialoclcs_letvariablecs = essentialoclcs_letvariablecs;
    }

}
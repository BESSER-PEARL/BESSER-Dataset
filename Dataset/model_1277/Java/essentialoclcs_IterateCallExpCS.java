





import java.util.List;
import java.util.ArrayList;

public class essentialoclcs_IterateCallExpCS extends IterationCallExpCS {






    private List<essentialoclcs_VariableCS> essentialoclcs_variablecss;


    public essentialoclcs_IterateCallExpCS(
    ) {
        super(
        );
        this.essentialoclcs_variablecss = new ArrayList<>();
    }

    public essentialoclcs_IterateCallExpCS(
        ArrayList<essentialoclcs_VariableCS> essentialoclcs_variablecss    ) {
        this.essentialoclcs_variablecss = essentialoclcs_variablecss;
    }


    public List<essentialoclcs_VariableCS> getEssentialoclcs_variablecss() {
        return essentialoclcs_variablecss;
    }

    public void addEssentialoclcs_variablecs(Essentialoclcs_variablecs essentialoclcs_variablecs) {
        this.essentialoclcs_variablecss.add(essentialoclcs_variablecs);
    }

}






import java.util.List;
import java.util.ArrayList;

public class p2_InstallableUnitFragment extends InstallableUnit, IInstallableUnitFragment {






    private List<p2_IRequirement> p2_irequirements;


    public p2_InstallableUnitFragment(
    ) {
        super(
        );
        this.p2_irequirements = new ArrayList<>();
    }

    public p2_InstallableUnitFragment(
        ArrayList<p2_IRequirement> p2_irequirements    ) {
        this.p2_irequirements = p2_irequirements;
    }


    public List<p2_IRequirement> getP2_irequirements() {
        return p2_irequirements;
    }

    public void addP2_irequirement(P2_irequirement p2_irequirement) {
        this.p2_irequirements.add(p2_irequirement);
    }

}
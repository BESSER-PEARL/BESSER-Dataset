





import java.util.List;
import java.util.ArrayList;

public class p2_IInstallableUnitPatch extends IInstallableUnit {






    private p2_IRequirement p2_irequirement;




    private List<p2_IRequirement> p2_irequirements;


    public p2_IInstallableUnitPatch(
    ) {
        super(
        );
        this.p2_irequirements = new ArrayList<>();
    }

    public p2_IInstallableUnitPatch(
        ArrayList<p2_IRequirement> p2_irequirements    ) {
        this.p2_irequirements = p2_irequirements;
    }


    public p2_IRequirement getP2_irequirement() {
        return p2_irequirement;
    }

    public void setP2_irequirement(p2_IRequirement p2_irequirement) {
        this.p2_irequirement = p2_irequirement;
    }
    public List<p2_IRequirement> getP2_irequirements() {
        return p2_irequirements;
    }

    public void addP2_irequirement(P2_irequirement p2_irequirement) {
        this.p2_irequirements.add(p2_irequirement);
    }

}
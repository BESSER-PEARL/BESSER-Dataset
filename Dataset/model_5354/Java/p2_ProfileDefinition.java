





import java.util.List;
import java.util.ArrayList;

public class p2_ProfileDefinition extends ModelElement {

    private boolean includeSourceBundles;





    private List<p2_Requirement> p2_requirements;


    public p2_ProfileDefinition(
        boolean includeSourceBundles    ) {
        super(
        );
        this.includeSourceBundles = includeSourceBundles;
        this.p2_requirements = new ArrayList<>();
    }

    public p2_ProfileDefinition(
        boolean includeSourceBundles        ArrayList<p2_Requirement> p2_requirements    ) {
        this.includeSourceBundles = includeSourceBundles;
        this.p2_requirements = p2_requirements;
    }

    public boolean getIncludesourcebundles() {
        return includeSourceBundles;
    }

    public void setIncludesourcebundles(boolean includeSourceBundles) {
        this.includeSourceBundles = includeSourceBundles;
    }

    public List<p2_Requirement> getP2_requirements() {
        return p2_requirements;
    }

    public void addP2_requirement(P2_requirement p2_requirement) {
        this.p2_requirements.add(p2_requirement);
    }

}
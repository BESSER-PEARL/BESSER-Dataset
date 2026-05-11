





import java.util.List;
import java.util.ArrayList;

public class core_COREImpactNode extends COREModelElement {

    private float offset;
    private float scalingFactor;





    private core_COREContribution core_corecontribution;




    private List<core_COREContribution> core_corecontributions;




    private core_COREContribution core_corecontribution;




    private core_COREInterface core_coreinterface;




    private List<core_COREContribution> core_corecontributions;


    public core_COREImpactNode(
        float offset,        float scalingFactor    ) {
        super(
        );
        this.offset = offset;
        this.scalingFactor = scalingFactor;
        this.core_corecontributions = new ArrayList<>();
        this.core_corecontributions = new ArrayList<>();
    }

    public core_COREImpactNode(
        float offset,        float scalingFactor        ArrayList<core_COREContribution> core_corecontributions,        ArrayList<core_COREContribution> core_corecontributions    ) {
        this.offset = offset;
        this.scalingFactor = scalingFactor;
        this.core_corecontributions = core_corecontributions;
        this.core_corecontributions = core_corecontributions;
    }

    public float getOffset() {
        return offset;
    }

    public void setOffset(float offset) {
        this.offset = offset;
    }
    public float getScalingfactor() {
        return scalingFactor;
    }

    public void setScalingfactor(float scalingFactor) {
        this.scalingFactor = scalingFactor;
    }

    public core_COREContribution getCore_corecontribution() {
        return core_corecontribution;
    }

    public void setCore_corecontribution(core_COREContribution core_corecontribution) {
        this.core_corecontribution = core_corecontribution;
    }
    public List<core_COREContribution> getCore_corecontributions() {
        return core_corecontributions;
    }

    public void addCore_corecontribution(Core_corecontribution core_corecontribution) {
        this.core_corecontributions.add(core_corecontribution);
    }
    public core_COREContribution getCore_corecontribution() {
        return core_corecontribution;
    }

    public void setCore_corecontribution(core_COREContribution core_corecontribution) {
        this.core_corecontribution = core_corecontribution;
    }
    public core_COREInterface getCore_coreinterface() {
        return core_coreinterface;
    }

    public void setCore_coreinterface(core_COREInterface core_coreinterface) {
        this.core_coreinterface = core_coreinterface;
    }
    public List<core_COREContribution> getCore_corecontributions() {
        return core_corecontributions;
    }

    public void addCore_corecontribution(Core_corecontribution core_corecontribution) {
        this.core_corecontributions.add(core_corecontribution);
    }

}
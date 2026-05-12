





import java.util.List;
import java.util.ArrayList;

public class gore_AwReq extends DefinableRequirement {

    private float incrementCoefficient;





    private List<gore_DefinableRequirement> gore_definablerequirements;




    private gore_DefinableRequirement gore_definablerequirement;


    public gore_AwReq(
        float incrementCoefficient    ) {
        super(
        );
        this.incrementCoefficient = incrementCoefficient;
        this.gore_definablerequirements = new ArrayList<>();
    }

    public gore_AwReq(
        float incrementCoefficient        ArrayList<gore_DefinableRequirement> gore_definablerequirements    ) {
        this.incrementCoefficient = incrementCoefficient;
        this.gore_definablerequirements = gore_definablerequirements;
    }

    public float getIncrementcoefficient() {
        return incrementCoefficient;
    }

    public void setIncrementcoefficient(float incrementCoefficient) {
        this.incrementCoefficient = incrementCoefficient;
    }

    public List<gore_DefinableRequirement> getGore_definablerequirements() {
        return gore_definablerequirements;
    }

    public void addGore_definablerequirement(Gore_definablerequirement gore_definablerequirement) {
        this.gore_definablerequirements.add(gore_definablerequirement);
    }
    public gore_DefinableRequirement getGore_definablerequirement() {
        return gore_definablerequirement;
    }

    public void setGore_definablerequirement(gore_DefinableRequirement gore_definablerequirement) {
        this.gore_definablerequirement = gore_definablerequirement;
    }

}
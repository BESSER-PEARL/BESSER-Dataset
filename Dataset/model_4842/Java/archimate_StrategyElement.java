





import java.util.List;
import java.util.ArrayList;

public class archimate_StrategyElement  {

    private String refinementType;
    private String relationType;
    private String name;





    private List<archimate_MotivationElement> archimate_motivationelements;




    private List<archimate_StrategyElement> archimate_strategyelements;


    public archimate_StrategyElement(
        String refinementType,        String relationType,        String name    ) {
        this.refinementType = refinementType;
        this.relationType = relationType;
        this.name = name;
        this.archimate_motivationelements = new ArrayList<>();
        this.archimate_strategyelements = new ArrayList<>();
    }

    public archimate_StrategyElement(
        String refinementType,        String relationType,        String name        ArrayList<archimate_MotivationElement> archimate_motivationelements,        ArrayList<archimate_StrategyElement> archimate_strategyelements    ) {
        this.refinementType = refinementType;
        this.relationType = relationType;
        this.name = name;
        this.archimate_motivationelements = archimate_motivationelements;
        this.archimate_strategyelements = archimate_strategyelements;
    }

    public String getRefinementtype() {
        return refinementType;
    }

    public void setRefinementtype(String refinementType) {
        this.refinementType = refinementType;
    }
    public String getRelationtype() {
        return relationType;
    }

    public void setRelationtype(String relationType) {
        this.relationType = relationType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<archimate_MotivationElement> getArchimate_motivationelements() {
        return archimate_motivationelements;
    }

    public void addArchimate_motivationelement(Archimate_motivationelement archimate_motivationelement) {
        this.archimate_motivationelements.add(archimate_motivationelement);
    }
    public List<archimate_StrategyElement> getArchimate_strategyelements() {
        return archimate_strategyelements;
    }

    public void addArchimate_strategyelement(Archimate_strategyelement archimate_strategyelement) {
        this.archimate_strategyelements.add(archimate_strategyelement);
    }

}
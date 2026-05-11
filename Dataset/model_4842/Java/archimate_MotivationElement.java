





import java.util.List;
import java.util.ArrayList;

public class archimate_MotivationElement  {

    private String refinementType;
    private String relationType;
    private String name;





    private List<archimate_MotivationElement> archimate_motivationelements;




    private archimate_MotivationElement archimate_motivationelement;




    private archimate_MotivationElement archimate_motivationelement;


    public archimate_MotivationElement(
        String refinementType,        String relationType,        String name    ) {
        this.refinementType = refinementType;
        this.relationType = relationType;
        this.name = name;
        this.archimate_motivationelements = new ArrayList<>();
    }

    public archimate_MotivationElement(
        String refinementType,        String relationType,        String name        ArrayList<archimate_MotivationElement> archimate_motivationelements    ) {
        this.refinementType = refinementType;
        this.relationType = relationType;
        this.name = name;
        this.archimate_motivationelements = archimate_motivationelements;
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
    public archimate_MotivationElement getArchimate_motivationelement() {
        return archimate_motivationelement;
    }

    public void setArchimate_motivationelement(archimate_MotivationElement archimate_motivationelement) {
        this.archimate_motivationelement = archimate_motivationelement;
    }
    public archimate_MotivationElement getArchimate_motivationelement() {
        return archimate_motivationelement;
    }

    public void setArchimate_motivationelement(archimate_MotivationElement archimate_motivationelement) {
        this.archimate_motivationelement = archimate_motivationelement;
    }

}
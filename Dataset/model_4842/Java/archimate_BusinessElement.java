





import java.util.List;
import java.util.ArrayList;

public class archimate_BusinessElement  {

    private String relationType;
    private String refinementType;
    private String name;





    private List<archimate_MotivationElement> archimate_motivationelements;




    private List<archimate_MotivationElement> archimate_motivationelements;




    private archimate_BusinessElement archimate_businesselement;




    private List<archimate_BusinessElement> archimate_businesselements;




    private List<archimate_MotivationElement> archimate_motivationelements;


    public archimate_BusinessElement(
        String relationType,        String refinementType,        String name    ) {
        this.relationType = relationType;
        this.refinementType = refinementType;
        this.name = name;
        this.archimate_motivationelements = new ArrayList<>();
        this.archimate_motivationelements = new ArrayList<>();
        this.archimate_businesselements = new ArrayList<>();
        this.archimate_motivationelements = new ArrayList<>();
    }

    public archimate_BusinessElement(
        String relationType,        String refinementType,        String name        ArrayList<archimate_MotivationElement> archimate_motivationelements,        ArrayList<archimate_MotivationElement> archimate_motivationelements,        ArrayList<archimate_BusinessElement> archimate_businesselements,        ArrayList<archimate_MotivationElement> archimate_motivationelements    ) {
        this.relationType = relationType;
        this.refinementType = refinementType;
        this.name = name;
        this.archimate_motivationelements = archimate_motivationelements;
        this.archimate_motivationelements = archimate_motivationelements;
        this.archimate_businesselements = archimate_businesselements;
        this.archimate_motivationelements = archimate_motivationelements;
    }

    public String getRelationtype() {
        return relationType;
    }

    public void setRelationtype(String relationType) {
        this.relationType = relationType;
    }
    public String getRefinementtype() {
        return refinementType;
    }

    public void setRefinementtype(String refinementType) {
        this.refinementType = refinementType;
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
    public List<archimate_MotivationElement> getArchimate_motivationelements() {
        return archimate_motivationelements;
    }

    public void addArchimate_motivationelement(Archimate_motivationelement archimate_motivationelement) {
        this.archimate_motivationelements.add(archimate_motivationelement);
    }
    public archimate_BusinessElement getArchimate_businesselement() {
        return archimate_businesselement;
    }

    public void setArchimate_businesselement(archimate_BusinessElement archimate_businesselement) {
        this.archimate_businesselement = archimate_businesselement;
    }
    public List<archimate_BusinessElement> getArchimate_businesselements() {
        return archimate_businesselements;
    }

    public void addArchimate_businesselement(Archimate_businesselement archimate_businesselement) {
        this.archimate_businesselements.add(archimate_businesselement);
    }
    public List<archimate_MotivationElement> getArchimate_motivationelements() {
        return archimate_motivationelements;
    }

    public void addArchimate_motivationelement(Archimate_motivationelement archimate_motivationelement) {
        this.archimate_motivationelements.add(archimate_motivationelement);
    }

}
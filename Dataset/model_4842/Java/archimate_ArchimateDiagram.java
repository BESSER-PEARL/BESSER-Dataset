





import java.util.List;
import java.util.ArrayList;

public class archimate_ArchimateDiagram  {






    private List<archimate_MotivationElement> archimate_motivationelements;




    private List<archimate_BusinessElement> archimate_businesselements;




    private List<archimate_StrategyElement> archimate_strategyelements;


    public archimate_ArchimateDiagram(
    ) {
        this.archimate_motivationelements = new ArrayList<>();
        this.archimate_businesselements = new ArrayList<>();
        this.archimate_strategyelements = new ArrayList<>();
    }

    public archimate_ArchimateDiagram(
        ArrayList<archimate_MotivationElement> archimate_motivationelements,        ArrayList<archimate_BusinessElement> archimate_businesselements,        ArrayList<archimate_StrategyElement> archimate_strategyelements    ) {
        this.archimate_motivationelements = archimate_motivationelements;
        this.archimate_businesselements = archimate_businesselements;
        this.archimate_strategyelements = archimate_strategyelements;
    }


    public List<archimate_MotivationElement> getArchimate_motivationelements() {
        return archimate_motivationelements;
    }

    public void addArchimate_motivationelement(Archimate_motivationelement archimate_motivationelement) {
        this.archimate_motivationelements.add(archimate_motivationelement);
    }
    public List<archimate_BusinessElement> getArchimate_businesselements() {
        return archimate_businesselements;
    }

    public void addArchimate_businesselement(Archimate_businesselement archimate_businesselement) {
        this.archimate_businesselements.add(archimate_businesselement);
    }
    public List<archimate_StrategyElement> getArchimate_strategyelements() {
        return archimate_strategyelements;
    }

    public void addArchimate_strategyelement(Archimate_strategyelement archimate_strategyelement) {
        this.archimate_strategyelements.add(archimate_strategyelement);
    }

}
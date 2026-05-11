





import java.util.List;
import java.util.ArrayList;

public class archimate_ActiveStructureElement  {

    private String name;





    private List<archimate_MotivationElement> archimate_motivationelements;




    private archimate_ArchimateDiagram archimate_archimatediagram;




    private List<archimate_ActiveStructureElement> archimate_activestructureelements;


    public archimate_ActiveStructureElement(
        String name    ) {
        this.name = name;
        this.archimate_motivationelements = new ArrayList<>();
        this.archimate_activestructureelements = new ArrayList<>();
    }

    public archimate_ActiveStructureElement(
        String name        ArrayList<archimate_MotivationElement> archimate_motivationelements,        ArrayList<archimate_ActiveStructureElement> archimate_activestructureelements    ) {
        this.name = name;
        this.archimate_motivationelements = archimate_motivationelements;
        this.archimate_activestructureelements = archimate_activestructureelements;
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
    public archimate_ArchimateDiagram getArchimate_archimatediagram() {
        return archimate_archimatediagram;
    }

    public void setArchimate_archimatediagram(archimate_ArchimateDiagram archimate_archimatediagram) {
        this.archimate_archimatediagram = archimate_archimatediagram;
    }
    public List<archimate_ActiveStructureElement> getArchimate_activestructureelements() {
        return archimate_activestructureelements;
    }

    public void addArchimate_activestructureelement(Archimate_activestructureelement archimate_activestructureelement) {
        this.archimate_activestructureelements.add(archimate_activestructureelement);
    }

}
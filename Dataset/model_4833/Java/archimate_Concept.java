





import java.util.List;
import java.util.ArrayList;

public class archimate_Concept  {

    private String name;
    private String description;





    private List<archimate_Concept> archimate_concepts;


    public archimate_Concept(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
        this.archimate_concepts = new ArrayList<>();
    }

    public archimate_Concept(
        String name,        String description        ArrayList<archimate_Concept> archimate_concepts    ) {
        this.name = name;
        this.description = description;
        this.archimate_concepts = archimate_concepts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<archimate_Concept> getArchimate_concepts() {
        return archimate_concepts;
    }

    public void addArchimate_concept(Archimate_concept archimate_concept) {
        this.archimate_concepts.add(archimate_concept);
    }

}
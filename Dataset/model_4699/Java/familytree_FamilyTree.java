





import java.util.List;
import java.util.ArrayList;

public class familytree_FamilyTree  {

    private String name;





    private List<familytree_Wedding> familytree_weddings;




    private List<familytree_Person> familytree_persons;


    public familytree_FamilyTree(
        String name    ) {
        this.name = name;
        this.familytree_weddings = new ArrayList<>();
        this.familytree_persons = new ArrayList<>();
    }

    public familytree_FamilyTree(
        String name        ArrayList<familytree_Wedding> familytree_weddings,        ArrayList<familytree_Person> familytree_persons    ) {
        this.name = name;
        this.familytree_weddings = familytree_weddings;
        this.familytree_persons = familytree_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<familytree_Wedding> getFamilytree_weddings() {
        return familytree_weddings;
    }

    public void addFamilytree_wedding(Familytree_wedding familytree_wedding) {
        this.familytree_weddings.add(familytree_wedding);
    }
    public List<familytree_Person> getFamilytree_persons() {
        return familytree_persons;
    }

    public void addFamilytree_person(Familytree_person familytree_person) {
        this.familytree_persons.add(familytree_person);
    }

}
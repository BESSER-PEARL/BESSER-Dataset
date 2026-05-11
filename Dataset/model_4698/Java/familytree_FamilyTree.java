





import java.util.List;
import java.util.ArrayList;

public class familytree_FamilyTree  {






    private List<familytree_Person> familytree_persons;


    public familytree_FamilyTree(
    ) {
        this.familytree_persons = new ArrayList<>();
    }

    public familytree_FamilyTree(
        ArrayList<familytree_Person> familytree_persons    ) {
        this.familytree_persons = familytree_persons;
    }


    public List<familytree_Person> getFamilytree_persons() {
        return familytree_persons;
    }

    public void addFamilytree_person(Familytree_person familytree_person) {
        this.familytree_persons.add(familytree_person);
    }

}
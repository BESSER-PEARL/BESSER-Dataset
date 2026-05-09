





import java.util.List;
import java.util.ArrayList;

public class Example_Family  {

    private String address;





    private List<Example_Pet> example_pets;




    private Example_Parent example_parent;




    private List<Example_Son> example_sons;




    private List<Example_Daughter> example_daughters;




    private List<Example_Parent> example_parents;




    private Example_Son example_son;




    private Example_Daughter example_daughter;


    public Example_Family(
        String address    ) {
        this.address = address;
        this.example_pets = new ArrayList<>();
        this.example_sons = new ArrayList<>();
        this.example_daughters = new ArrayList<>();
        this.example_parents = new ArrayList<>();
    }

    public Example_Family(
        String address        ArrayList<Example_Pet> example_pets,        ArrayList<Example_Son> example_sons,        ArrayList<Example_Daughter> example_daughters,        ArrayList<Example_Parent> example_parents    ) {
        this.address = address;
        this.example_pets = example_pets;
        this.example_sons = example_sons;
        this.example_daughters = example_daughters;
        this.example_parents = example_parents;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public List<Example_Pet> getExample_pets() {
        return example_pets;
    }

    public void addExample_pet(Example_pet example_pet) {
        this.example_pets.add(example_pet);
    }
    public Example_Parent getExample_parent() {
        return example_parent;
    }

    public void setExample_parent(Example_Parent example_parent) {
        this.example_parent = example_parent;
    }
    public List<Example_Son> getExample_sons() {
        return example_sons;
    }

    public void addExample_son(Example_son example_son) {
        this.example_sons.add(example_son);
    }
    public List<Example_Daughter> getExample_daughters() {
        return example_daughters;
    }

    public void addExample_daughter(Example_daughter example_daughter) {
        this.example_daughters.add(example_daughter);
    }
    public List<Example_Parent> getExample_parents() {
        return example_parents;
    }

    public void addExample_parent(Example_parent example_parent) {
        this.example_parents.add(example_parent);
    }
    public Example_Son getExample_son() {
        return example_son;
    }

    public void setExample_son(Example_Son example_son) {
        this.example_son = example_son;
    }
    public Example_Daughter getExample_daughter() {
        return example_daughter;
    }

    public void setExample_daughter(Example_Daughter example_daughter) {
        this.example_daughter = example_daughter;
    }

}
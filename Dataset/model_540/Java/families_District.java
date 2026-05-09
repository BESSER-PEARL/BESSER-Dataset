





import java.util.List;
import java.util.ArrayList;

public class families_District  {






    private List<families_Family> families_familys;




    private families_Family families_family;




    private List<families_Dog> families_dogs;




    private families_Dog families_dog;


    public families_District(
    ) {
        this.families_familys = new ArrayList<>();
        this.families_dogs = new ArrayList<>();
    }

    public families_District(
        ArrayList<families_Family> families_familys,        ArrayList<families_Dog> families_dogs    ) {
        this.families_familys = families_familys;
        this.families_dogs = families_dogs;
    }


    public List<families_Family> getFamilies_familys() {
        return families_familys;
    }

    public void addFamilies_family(Families_family families_family) {
        this.families_familys.add(families_family);
    }
    public families_Family getFamilies_family() {
        return families_family;
    }

    public void setFamilies_family(families_Family families_family) {
        this.families_family = families_family;
    }
    public List<families_Dog> getFamilies_dogs() {
        return families_dogs;
    }

    public void addFamilies_dog(Families_dog families_dog) {
        this.families_dogs.add(families_dog);
    }
    public families_Dog getFamilies_dog() {
        return families_dog;
    }

    public void setFamilies_dog(families_Dog families_dog) {
        this.families_dog = families_dog;
    }

}
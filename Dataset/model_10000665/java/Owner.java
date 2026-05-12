





import java.util.List;
import java.util.ArrayList;

public class Owner  {






    private List<Dog> dogs;


    public Owner(
    ) {
        this.dogs = new ArrayList<>();
    }

    public Owner(
        ArrayList<Dog> dogs    ) {
        this.dogs = dogs;
    }


    public List<Dog> getDogs() {
        return dogs;
    }

    public void addDog(Dog dog) {
        this.dogs.add(dog);
    }

}






import java.util.List;
import java.util.ArrayList;

public class Example_Pet  {

    private String breed;
    private String name;





    private Example_Family example_family;


    public Example_Pet(
        String breed,        String name    ) {
        this.breed = breed;
        this.name = name;
    }


    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Example_Family getExample_family() {
        return example_family;
    }

    public void setExample_family(Example_Family example_family) {
        this.example_family = example_family;
    }

}
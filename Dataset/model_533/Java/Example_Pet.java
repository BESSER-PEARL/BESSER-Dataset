





import java.util.List;
import java.util.ArrayList;

public class Example_Pet  {

    private String name;
    private String breed;



    public Example_Pet(
        String name,        String breed    ) {
        this.name = name;
        this.breed = breed;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }


}
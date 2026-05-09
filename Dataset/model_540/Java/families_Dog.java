





import java.util.List;
import java.util.ArrayList;

public class families_Dog extends Pet {

    private boolean loud;
    private String breed;





    private families_Family families_family;


    public families_Dog(
        boolean loud,        String breed    ) {
        super(
        );
        this.loud = loud;
        this.breed = breed;
    }


    public boolean getLoud() {
        return loud;
    }

    public void setLoud(boolean loud) {
        this.loud = loud;
    }
    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }

    public families_Family getFamilies_family() {
        return families_family;
    }

    public void setFamilies_family(families_Family families_family) {
        this.families_family = families_family;
    }

}
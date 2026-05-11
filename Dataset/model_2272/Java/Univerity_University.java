





import java.util.List;
import java.util.ArrayList;

public class Univerity_University  {






    private List<Univerity_Courses> univerity_coursess;


    public Univerity_University(
    ) {
        this.univerity_coursess = new ArrayList<>();
    }

    public Univerity_University(
        ArrayList<Univerity_Courses> univerity_coursess    ) {
        this.univerity_coursess = univerity_coursess;
    }


    public List<Univerity_Courses> getUniverity_coursess() {
        return univerity_coursess;
    }

    public void addUniverity_courses(Univerity_courses univerity_courses) {
        this.univerity_coursess.add(univerity_courses);
    }

}
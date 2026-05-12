





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_MainComposition  {






    private reqLanguage_System reqlanguage_system;




    private List<reqLanguage_System> reqlanguage_systems;


    public reqLanguage_MainComposition(
    ) {
        this.reqlanguage_systems = new ArrayList<>();
    }

    public reqLanguage_MainComposition(
        ArrayList<reqLanguage_System> reqlanguage_systems    ) {
        this.reqlanguage_systems = reqlanguage_systems;
    }


    public reqLanguage_System getReqlanguage_system() {
        return reqlanguage_system;
    }

    public void setReqlanguage_system(reqLanguage_System reqlanguage_system) {
        this.reqlanguage_system = reqlanguage_system;
    }
    public List<reqLanguage_System> getReqlanguage_systems() {
        return reqlanguage_systems;
    }

    public void addReqlanguage_system(Reqlanguage_system reqlanguage_system) {
        this.reqlanguage_systems.add(reqlanguage_system);
    }

}
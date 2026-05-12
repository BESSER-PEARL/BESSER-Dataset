





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_Actor  {

    private String actor;
    private String name;



    public reqLanguage_Actor(
        String actor,        String name    ) {
        this.actor = actor;
        this.name = name;
    }


    public String getActor() {
        return actor;
    }

    public void setActor(String actor) {
        this.actor = actor;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
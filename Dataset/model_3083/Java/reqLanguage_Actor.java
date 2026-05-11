





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_Actor  {

    private String name;
    private String actor;



    public reqLanguage_Actor(
        String name,        String actor    ) {
        this.name = name;
        this.actor = actor;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getActor() {
        return actor;
    }

    public void setActor(String actor) {
        this.actor = actor;
    }


}
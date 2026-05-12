





import java.util.List;
import java.util.ArrayList;

public class Ant_Project  {

    private String name;
    private String basedir;
    private String description;



    public Ant_Project(
        String name,        String basedir,        String description    ) {
        this.name = name;
        this.basedir = basedir;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBasedir() {
        return basedir;
    }

    public void setBasedir(String basedir) {
        this.basedir = basedir;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}
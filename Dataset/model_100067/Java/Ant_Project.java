





import java.util.List;
import java.util.ArrayList;

public class Ant_Project  {

    private String name;
    private String description;
    private String basedir;



    public Ant_Project(
        String name,        String description,        String basedir    ) {
        this.name = name;
        this.description = description;
        this.basedir = basedir;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getBasedir() {
        return basedir;
    }

    public void setBasedir(String basedir) {
        this.basedir = basedir;
    }


}
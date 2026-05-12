





import java.util.List;
import java.util.ArrayList;

public class Ant_Project  {

    private String description;
    private String name;
    private String basedir;



    public Ant_Project(
        String description,        String name,        String basedir    ) {
        this.description = description;
        this.name = name;
        this.basedir = basedir;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
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


}
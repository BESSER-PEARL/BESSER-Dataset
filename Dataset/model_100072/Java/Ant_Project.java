





import java.util.List;
import java.util.ArrayList;

public class Ant_Project  {

    private String basedir;
    private String description;
    private String name;



    public Ant_Project(
        String basedir,        String description,        String name    ) {
        this.basedir = basedir;
        this.description = description;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
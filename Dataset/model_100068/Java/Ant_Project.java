





import java.util.List;
import java.util.ArrayList;

public class Ant_Project  {

    private String basedir;
    private String name;
    private String description;





    private Path path;


    public Ant_Project(
        String basedir,        String name,        String description    ) {
        this.basedir = basedir;
        this.name = name;
        this.description = description;
    }


    public String getBasedir() {
        return basedir;
    }

    public void setBasedir(String basedir) {
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

    public Path getPath() {
        return path;
    }

    public void setPath(Path path) {
        this.path = path;
    }

}
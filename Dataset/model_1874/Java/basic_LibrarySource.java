





import java.util.List;
import java.util.ArrayList;

public class basic_LibrarySource  {

    private String exclusions;
    private String type;
    private String path;
    private String inclusions;





    private List<basic_File> basic_files;


    public basic_LibrarySource(
        String exclusions,        String type,        String path,        String inclusions    ) {
        this.exclusions = exclusions;
        this.type = type;
        this.path = path;
        this.inclusions = inclusions;
        this.basic_files = new ArrayList<>();
    }

    public basic_LibrarySource(
        String exclusions,        String type,        String path,        String inclusions        ArrayList<basic_File> basic_files    ) {
        this.exclusions = exclusions;
        this.type = type;
        this.path = path;
        this.inclusions = inclusions;
        this.basic_files = basic_files;
    }

    public String getExclusions() {
        return exclusions;
    }

    public void setExclusions(String exclusions) {
        this.exclusions = exclusions;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getInclusions() {
        return inclusions;
    }

    public void setInclusions(String inclusions) {
        this.inclusions = inclusions;
    }

    public List<basic_File> getBasic_files() {
        return basic_files;
    }

    public void addBasic_file(Basic_file basic_file) {
        this.basic_files.add(basic_file);
    }

}
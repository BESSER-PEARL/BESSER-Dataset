





import java.util.List;
import java.util.ArrayList;

public class sxfm_Feature  {

    private String description;
    private String name;
    private int treeLevel;
    private String id;



    public sxfm_Feature(
        String description,        String name,        int treeLevel,        String id    ) {
        this.description = description;
        this.name = name;
        this.treeLevel = treeLevel;
        this.id = id;
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
    public int getTreelevel() {
        return treeLevel;
    }

    public void setTreelevel(int treeLevel) {
        this.treeLevel = treeLevel;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}
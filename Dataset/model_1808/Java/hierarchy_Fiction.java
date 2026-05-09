





import java.util.List;
import java.util.ArrayList;

public class hierarchy_Fiction  {

    private String Name;





    private hierarchy_HierLibrary hierarchy_hierlibrary;


    public hierarchy_Fiction(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public hierarchy_HierLibrary getHierarchy_hierlibrary() {
        return hierarchy_hierlibrary;
    }

    public void setHierarchy_hierlibrary(hierarchy_HierLibrary hierarchy_hierlibrary) {
        this.hierarchy_hierlibrary = hierarchy_hierlibrary;
    }

}
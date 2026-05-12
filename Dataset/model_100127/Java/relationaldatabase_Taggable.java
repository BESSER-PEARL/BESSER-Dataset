





import java.util.List;
import java.util.ArrayList;

public class relationaldatabase_Taggable  {






    private List<relationaldatabase_Tag> relationaldatabase_tags;


    public relationaldatabase_Taggable(
    ) {
        this.relationaldatabase_tags = new ArrayList<>();
    }

    public relationaldatabase_Taggable(
        ArrayList<relationaldatabase_Tag> relationaldatabase_tags    ) {
        this.relationaldatabase_tags = relationaldatabase_tags;
    }


    public List<relationaldatabase_Tag> getRelationaldatabase_tags() {
        return relationaldatabase_tags;
    }

    public void addRelationaldatabase_tag(Relationaldatabase_tag relationaldatabase_tag) {
        this.relationaldatabase_tags.add(relationaldatabase_tag);
    }

}
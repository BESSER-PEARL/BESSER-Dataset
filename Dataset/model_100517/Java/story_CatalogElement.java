





import java.util.List;
import java.util.ArrayList;

public class story_CatalogElement  {

    private String id;
    private String name;
    private String description;





    private story_Catalog story_catalog;


    public story_CatalogElement(
        String id,        String name,        String description    ) {
        this.id = id;
        this.name = name;
        this.description = description;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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

    public story_Catalog getStory_catalog() {
        return story_catalog;
    }

    public void setStory_catalog(story_Catalog story_catalog) {
        this.story_catalog = story_catalog;
    }

}






import java.util.List;
import java.util.ArrayList;

public class forms_entityModeling_Form  {

    private String name;
    private String description;
    private String title;





    private Entity entity;


    public forms_entityModeling_Form(
        String name,        String description,        String title    ) {
        this.name = name;
        this.description = description;
        this.title = title;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Entity getEntity() {
        return entity;
    }

    public void setEntity(Entity entity) {
        this.entity = entity;
    }

}
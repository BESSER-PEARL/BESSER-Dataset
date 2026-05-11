





import java.util.List;
import java.util.ArrayList;

public class camel_Application  {

    private String version;
    private String description;
    private String name;





    private Entity entity;




    private camel_CamelModel camel_camelmodel;


    public camel_Application(
        String version,        String description,        String name    ) {
        this.version = version;
        this.description = description;
        this.name = name;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
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

    public Entity getEntity() {
        return entity;
    }

    public void setEntity(Entity entity) {
        this.entity = entity;
    }
    public camel_CamelModel getCamel_camelmodel() {
        return camel_camelmodel;
    }

    public void setCamel_camelmodel(camel_CamelModel camel_camelmodel) {
        this.camel_camelmodel = camel_camelmodel;
    }

}






import java.util.List;
import java.util.ArrayList;

public class xwiki_Wiki extends LinkCollection {

    private String id;
    private String owner;
    private String name;
    private String description;



    public xwiki_Wiki(
        String id,        String owner,        String name,        String description    ) {
        super(
        );
        this.id = id;
        this.owner = owner;
        this.name = name;
        this.description = description;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
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


}
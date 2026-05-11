





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Container  {

    private String description;
    private String name;
    private String id;





    private contentfwk_Container contentfwk_container;


    public contentfwk_Container(
        String description,        String name,        String id    ) {
        this.description = description;
        this.name = name;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public contentfwk_Container getContentfwk_container() {
        return contentfwk_container;
    }

    public void setContentfwk_container(contentfwk_Container contentfwk_container) {
        this.contentfwk_container = contentfwk_container;
    }

}
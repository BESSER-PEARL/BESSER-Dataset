





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Label  {

    private String id;
    private String name;
    private String description;





    private List<contentfwk_Container> contentfwk_containers;




    private List<contentfwk_Label> contentfwk_labels;




    private contentfwk_Container contentfwk_container;


    public contentfwk_Label(
        String id,        String name,        String description    ) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.contentfwk_containers = new ArrayList<>();
        this.contentfwk_labels = new ArrayList<>();
    }

    public contentfwk_Label(
        String id,        String name,        String description        ArrayList<contentfwk_Container> contentfwk_containers,        ArrayList<contentfwk_Label> contentfwk_labels    ) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.contentfwk_containers = contentfwk_containers;
        this.contentfwk_labels = contentfwk_labels;
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

    public List<contentfwk_Container> getContentfwk_containers() {
        return contentfwk_containers;
    }

    public void addContentfwk_container(Contentfwk_container contentfwk_container) {
        this.contentfwk_containers.add(contentfwk_container);
    }
    public List<contentfwk_Label> getContentfwk_labels() {
        return contentfwk_labels;
    }

    public void addContentfwk_label(Contentfwk_label contentfwk_label) {
        this.contentfwk_labels.add(contentfwk_label);
    }
    public contentfwk_Container getContentfwk_container() {
        return contentfwk_container;
    }

    public void setContentfwk_container(contentfwk_Container contentfwk_container) {
        this.contentfwk_container = contentfwk_container;
    }

}
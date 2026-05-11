





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Label  {

    private String description;
    private String name;
    private String id;





    private contentfwk_Element contentfwk_element;




    private List<contentfwk_Container> contentfwk_containers;




    private contentfwk_Label contentfwk_label;




    private contentfwk_EnterpriseArchitecture contentfwk_enterprisearchitecture;




    private List<contentfwk_Element> contentfwk_elements;




    private contentfwk_Container contentfwk_container;


    public contentfwk_Label(
        String description,        String name,        String id    ) {
        this.description = description;
        this.name = name;
        this.id = id;
        this.contentfwk_containers = new ArrayList<>();
        this.contentfwk_elements = new ArrayList<>();
    }

    public contentfwk_Label(
        String description,        String name,        String id        ArrayList<contentfwk_Container> contentfwk_containers,        ArrayList<contentfwk_Element> contentfwk_elements    ) {
        this.description = description;
        this.name = name;
        this.id = id;
        this.contentfwk_containers = contentfwk_containers;
        this.contentfwk_elements = contentfwk_elements;
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

    public contentfwk_Element getContentfwk_element() {
        return contentfwk_element;
    }

    public void setContentfwk_element(contentfwk_Element contentfwk_element) {
        this.contentfwk_element = contentfwk_element;
    }
    public List<contentfwk_Container> getContentfwk_containers() {
        return contentfwk_containers;
    }

    public void addContentfwk_container(Contentfwk_container contentfwk_container) {
        this.contentfwk_containers.add(contentfwk_container);
    }
    public contentfwk_Label getContentfwk_label() {
        return contentfwk_label;
    }

    public void setContentfwk_label(contentfwk_Label contentfwk_label) {
        this.contentfwk_label = contentfwk_label;
    }
    public contentfwk_EnterpriseArchitecture getContentfwk_enterprisearchitecture() {
        return contentfwk_enterprisearchitecture;
    }

    public void setContentfwk_enterprisearchitecture(contentfwk_EnterpriseArchitecture contentfwk_enterprisearchitecture) {
        this.contentfwk_enterprisearchitecture = contentfwk_enterprisearchitecture;
    }
    public List<contentfwk_Element> getContentfwk_elements() {
        return contentfwk_elements;
    }

    public void addContentfwk_element(Contentfwk_element contentfwk_element) {
        this.contentfwk_elements.add(contentfwk_element);
    }
    public contentfwk_Container getContentfwk_container() {
        return contentfwk_container;
    }

    public void setContentfwk_container(contentfwk_Container contentfwk_container) {
        this.contentfwk_container = contentfwk_container;
    }

}
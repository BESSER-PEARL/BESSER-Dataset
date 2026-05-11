





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Element  {

    private String name;
    private String sourceDescr;
    private String category;
    private String description;
    private String ID;
    private String ownerDescr;





    private List<contentfwk_Element> contentfwk_elements;




    private List<contentfwk_Element> contentfwk_elements;


    public contentfwk_Element(
        String name,        String sourceDescr,        String category,        String description,        String ID,        String ownerDescr    ) {
        this.name = name;
        this.sourceDescr = sourceDescr;
        this.category = category;
        this.description = description;
        this.ID = ID;
        this.ownerDescr = ownerDescr;
        this.contentfwk_elements = new ArrayList<>();
        this.contentfwk_elements = new ArrayList<>();
    }

    public contentfwk_Element(
        String name,        String sourceDescr,        String category,        String description,        String ID,        String ownerDescr        ArrayList<contentfwk_Element> contentfwk_elements,        ArrayList<contentfwk_Element> contentfwk_elements    ) {
        this.name = name;
        this.sourceDescr = sourceDescr;
        this.category = category;
        this.description = description;
        this.ID = ID;
        this.ownerDescr = ownerDescr;
        this.contentfwk_elements = contentfwk_elements;
        this.contentfwk_elements = contentfwk_elements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSourcedescr() {
        return sourceDescr;
    }

    public void setSourcedescr(String sourceDescr) {
        this.sourceDescr = sourceDescr;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getOwnerdescr() {
        return ownerDescr;
    }

    public void setOwnerdescr(String ownerDescr) {
        this.ownerDescr = ownerDescr;
    }

    public List<contentfwk_Element> getContentfwk_elements() {
        return contentfwk_elements;
    }

    public void addContentfwk_element(Contentfwk_element contentfwk_element) {
        this.contentfwk_elements.add(contentfwk_element);
    }
    public List<contentfwk_Element> getContentfwk_elements() {
        return contentfwk_elements;
    }

    public void addContentfwk_element(Contentfwk_element contentfwk_element) {
        this.contentfwk_elements.add(contentfwk_element);
    }

}
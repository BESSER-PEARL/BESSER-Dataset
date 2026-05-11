





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Element  {

    private String ownerDescr;
    private String name;
    private String sourceDescr;
    private String ID;
    private String category;
    private String description;





    private contentfwk_Element contentfwk_element;




    private List<contentfwk_Element> contentfwk_elements;


    public contentfwk_Element(
        String ownerDescr,        String name,        String sourceDescr,        String ID,        String category,        String description    ) {
        this.ownerDescr = ownerDescr;
        this.name = name;
        this.sourceDescr = sourceDescr;
        this.ID = ID;
        this.category = category;
        this.description = description;
        this.contentfwk_elements = new ArrayList<>();
    }

    public contentfwk_Element(
        String ownerDescr,        String name,        String sourceDescr,        String ID,        String category,        String description        ArrayList<contentfwk_Element> contentfwk_elements    ) {
        this.ownerDescr = ownerDescr;
        this.name = name;
        this.sourceDescr = sourceDescr;
        this.ID = ID;
        this.category = category;
        this.description = description;
        this.contentfwk_elements = contentfwk_elements;
    }

    public String getOwnerdescr() {
        return ownerDescr;
    }

    public void setOwnerdescr(String ownerDescr) {
        this.ownerDescr = ownerDescr;
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
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
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

    public contentfwk_Element getContentfwk_element() {
        return contentfwk_element;
    }

    public void setContentfwk_element(contentfwk_Element contentfwk_element) {
        this.contentfwk_element = contentfwk_element;
    }
    public List<contentfwk_Element> getContentfwk_elements() {
        return contentfwk_elements;
    }

    public void addContentfwk_element(Contentfwk_element contentfwk_element) {
        this.contentfwk_elements.add(contentfwk_element);
    }

}






import java.util.List;
import java.util.ArrayList;

public class contentfwk_Element  {

    private String description;
    private String sourceDescr;
    private String ID;
    private String ownerDescr;
    private String name;





    private List<contentfwk_Element> contentfwk_elements;




    private List<contentfwk_Element> contentfwk_elements;


    public contentfwk_Element(
        String description,        String sourceDescr,        String ID,        String ownerDescr,        String name    ) {
        this.description = description;
        this.sourceDescr = sourceDescr;
        this.ID = ID;
        this.ownerDescr = ownerDescr;
        this.name = name;
        this.contentfwk_elements = new ArrayList<>();
        this.contentfwk_elements = new ArrayList<>();
    }

    public contentfwk_Element(
        String description,        String sourceDescr,        String ID,        String ownerDescr,        String name        ArrayList<contentfwk_Element> contentfwk_elements,        ArrayList<contentfwk_Element> contentfwk_elements    ) {
        this.description = description;
        this.sourceDescr = sourceDescr;
        this.ID = ID;
        this.ownerDescr = ownerDescr;
        this.name = name;
        this.contentfwk_elements = contentfwk_elements;
        this.contentfwk_elements = contentfwk_elements;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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
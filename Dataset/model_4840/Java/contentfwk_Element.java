





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Element  {

    private String description;
    private String name;
    private String sourceDescr;
    private String ID;
    private String ownerDescr;





    private List<contentfwk_Label> contentfwk_labels;




    private List<contentfwk_Element> contentfwk_elements;




    private contentfwk_Element contentfwk_element;




    private contentfwk_Label contentfwk_label;


    public contentfwk_Element(
        String description,        String name,        String sourceDescr,        String ID,        String ownerDescr    ) {
        this.description = description;
        this.name = name;
        this.sourceDescr = sourceDescr;
        this.ID = ID;
        this.ownerDescr = ownerDescr;
        this.contentfwk_labels = new ArrayList<>();
        this.contentfwk_elements = new ArrayList<>();
    }

    public contentfwk_Element(
        String description,        String name,        String sourceDescr,        String ID,        String ownerDescr        ArrayList<contentfwk_Label> contentfwk_labels,        ArrayList<contentfwk_Element> contentfwk_elements    ) {
        this.description = description;
        this.name = name;
        this.sourceDescr = sourceDescr;
        this.ID = ID;
        this.ownerDescr = ownerDescr;
        this.contentfwk_labels = contentfwk_labels;
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

    public List<contentfwk_Label> getContentfwk_labels() {
        return contentfwk_labels;
    }

    public void addContentfwk_label(Contentfwk_label contentfwk_label) {
        this.contentfwk_labels.add(contentfwk_label);
    }
    public List<contentfwk_Element> getContentfwk_elements() {
        return contentfwk_elements;
    }

    public void addContentfwk_element(Contentfwk_element contentfwk_element) {
        this.contentfwk_elements.add(contentfwk_element);
    }
    public contentfwk_Element getContentfwk_element() {
        return contentfwk_element;
    }

    public void setContentfwk_element(contentfwk_Element contentfwk_element) {
        this.contentfwk_element = contentfwk_element;
    }
    public contentfwk_Label getContentfwk_label() {
        return contentfwk_label;
    }

    public void setContentfwk_label(contentfwk_Label contentfwk_label) {
        this.contentfwk_label = contentfwk_label;
    }

}
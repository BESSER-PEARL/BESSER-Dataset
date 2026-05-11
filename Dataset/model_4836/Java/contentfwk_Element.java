





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Element  {

    private String ID;
    private String description;
    private String ownerDescr;
    private String category;
    private String name;
    private String sourceDescr;





    private contentfwk_Element contentfwk_element;




    private contentfwk_Container contentfwk_container;




    private contentfwk_Element contentfwk_element;


    public contentfwk_Element(
        String ID,        String description,        String ownerDescr,        String category,        String name,        String sourceDescr    ) {
        this.ID = ID;
        this.description = description;
        this.ownerDescr = ownerDescr;
        this.category = category;
        this.name = name;
        this.sourceDescr = sourceDescr;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getOwnerdescr() {
        return ownerDescr;
    }

    public void setOwnerdescr(String ownerDescr) {
        this.ownerDescr = ownerDescr;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
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

    public contentfwk_Element getContentfwk_element() {
        return contentfwk_element;
    }

    public void setContentfwk_element(contentfwk_Element contentfwk_element) {
        this.contentfwk_element = contentfwk_element;
    }
    public contentfwk_Container getContentfwk_container() {
        return contentfwk_container;
    }

    public void setContentfwk_container(contentfwk_Container contentfwk_container) {
        this.contentfwk_container = contentfwk_container;
    }
    public contentfwk_Element getContentfwk_element() {
        return contentfwk_element;
    }

    public void setContentfwk_element(contentfwk_Element contentfwk_element) {
        this.contentfwk_element = contentfwk_element;
    }

}
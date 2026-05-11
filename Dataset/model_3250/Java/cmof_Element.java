





import java.util.List;
import java.util.ArrayList;

public class cmof_Element extends Object {






    private cmof_Link cmof_link;




    private cmof_Element cmof_element;




    private List<cmof_Element> cmof_elements;




    private cmof_Link cmof_link;


    public cmof_Element(
    ) {
        super(
        );
        this.cmof_elements = new ArrayList<>();
    }

    public cmof_Element(
        ArrayList<cmof_Element> cmof_elements    ) {
        this.cmof_elements = cmof_elements;
    }


    public cmof_Link getCmof_link() {
        return cmof_link;
    }

    public void setCmof_link(cmof_Link cmof_link) {
        this.cmof_link = cmof_link;
    }
    public cmof_Element getCmof_element() {
        return cmof_element;
    }

    public void setCmof_element(cmof_Element cmof_element) {
        this.cmof_element = cmof_element;
    }
    public List<cmof_Element> getCmof_elements() {
        return cmof_elements;
    }

    public void addCmof_element(Cmof_element cmof_element) {
        this.cmof_elements.add(cmof_element);
    }
    public cmof_Link getCmof_link() {
        return cmof_link;
    }

    public void setCmof_link(cmof_Link cmof_link) {
        this.cmof_link = cmof_link;
    }

}
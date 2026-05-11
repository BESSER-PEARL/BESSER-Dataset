





import java.util.List;
import java.util.ArrayList;

public class cmof_Element  {






    private cmof_Constraint cmof_constraint;




    private List<cmof_Element> cmof_elements;




    private cmof_Element cmof_element;


    public cmof_Element(
    ) {
        this.cmof_elements = new ArrayList<>();
    }

    public cmof_Element(
        ArrayList<cmof_Element> cmof_elements    ) {
        this.cmof_elements = cmof_elements;
    }


    public cmof_Constraint getCmof_constraint() {
        return cmof_constraint;
    }

    public void setCmof_constraint(cmof_Constraint cmof_constraint) {
        this.cmof_constraint = cmof_constraint;
    }
    public List<cmof_Element> getCmof_elements() {
        return cmof_elements;
    }

    public void addCmof_element(Cmof_element cmof_element) {
        this.cmof_elements.add(cmof_element);
    }
    public cmof_Element getCmof_element() {
        return cmof_element;
    }

    public void setCmof_element(cmof_Element cmof_element) {
        this.cmof_element = cmof_element;
    }

}
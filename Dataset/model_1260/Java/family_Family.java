





import java.util.List;
import java.util.ArrayList;

public class family_Family extends NamedElement {

    private String children;
    private String father;
    private String mother;



    public family_Family(
        String children,        String father,        String mother    ) {
        super(
        );
        this.children = children;
        this.father = father;
        this.mother = mother;
    }


    public String getChildren() {
        return children;
    }

    public void setChildren(String children) {
        this.children = children;
    }
    public String getFather() {
        return father;
    }

    public void setFather(String father) {
        this.father = father;
    }
    public String getMother() {
        return mother;
    }

    public void setMother(String mother) {
        this.mother = mother;
    }


}
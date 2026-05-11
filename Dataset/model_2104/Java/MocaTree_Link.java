





import java.util.List;
import java.util.ArrayList;

public class MocaTree_Link extends TreeElement {






    private List<MocaTree_Attribute> mocatree_attributes;


    public MocaTree_Link(
    ) {
        super(
        );
        this.mocatree_attributes = new ArrayList<>();
    }

    public MocaTree_Link(
        ArrayList<MocaTree_Attribute> mocatree_attributes    ) {
        this.mocatree_attributes = mocatree_attributes;
    }


    public List<MocaTree_Attribute> getMocatree_attributes() {
        return mocatree_attributes;
    }

    public void addMocatree_attribute(Mocatree_attribute mocatree_attribute) {
        this.mocatree_attributes.add(mocatree_attribute);
    }

}
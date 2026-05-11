





import java.util.List;
import java.util.ArrayList;

public class limp_SomeAttributeBlock extends AttributeBlock {






    private List<limp_Attribute> limp_attributes;


    public limp_SomeAttributeBlock(
    ) {
        super(
        );
        this.limp_attributes = new ArrayList<>();
    }

    public limp_SomeAttributeBlock(
        ArrayList<limp_Attribute> limp_attributes    ) {
        this.limp_attributes = limp_attributes;
    }


    public List<limp_Attribute> getLimp_attributes() {
        return limp_attributes;
    }

    public void addLimp_attribute(Limp_attribute limp_attribute) {
        this.limp_attributes.add(limp_attribute);
    }

}
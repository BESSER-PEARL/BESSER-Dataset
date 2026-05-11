





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_collaborations_AssociationEndRole extends AssociationEnd {






    private List<Attribute> attributes;


    public behavioral_elements_collaborations_AssociationEndRole(
    ) {
        super(
        );
        this.attributes = new ArrayList<>();
    }

    public behavioral_elements_collaborations_AssociationEndRole(
        ArrayList<Attribute> attributes    ) {
        this.attributes = attributes;
    }


    public List<Attribute> getAttributes() {
        return attributes;
    }

    public void addAttribute(Attribute attribute) {
        this.attributes.add(attribute);
    }

}
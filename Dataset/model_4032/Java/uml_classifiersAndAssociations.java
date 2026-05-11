





import java.util.List;
import java.util.ArrayList;

public class uml_classifiersAndAssociations  {

    private String group;





    private List<uml_association> uml_associations;


    public uml_classifiersAndAssociations(
        String group    ) {
        this.group = group;
        this.uml_associations = new ArrayList<>();
    }

    public uml_classifiersAndAssociations(
        String group        ArrayList<uml_association> uml_associations    ) {
        this.group = group;
        this.uml_associations = uml_associations;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<uml_association> getUml_associations() {
        return uml_associations;
    }

    public void addUml_association(Uml_association uml_association) {
        this.uml_associations.add(uml_association);
    }

}
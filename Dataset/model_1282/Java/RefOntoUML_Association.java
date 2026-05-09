





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Association extends Relationship, Classifier {

    private String isDerived;





    private List<RefOntoUML_Type> refontouml_types;


    public RefOntoUML_Association(
        String isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
        this.refontouml_types = new ArrayList<>();
    }

    public RefOntoUML_Association(
        String isDerived        ArrayList<RefOntoUML_Type> refontouml_types    ) {
        this.isDerived = isDerived;
        this.refontouml_types = refontouml_types;
    }

    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }

    public List<RefOntoUML_Type> getRefontouml_types() {
        return refontouml_types;
    }

    public void addRefontouml_type(Refontouml_type refontouml_type) {
        this.refontouml_types.add(refontouml_type);
    }

}
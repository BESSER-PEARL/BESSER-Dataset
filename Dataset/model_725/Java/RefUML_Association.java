





import java.util.List;
import java.util.ArrayList;

public class RefUML_Association extends Relationship, Classifier {

    private String isDerived;





    private List<RefUML_Type> refuml_types;


    public RefUML_Association(
        String isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
        this.refuml_types = new ArrayList<>();
    }

    public RefUML_Association(
        String isDerived        ArrayList<RefUML_Type> refuml_types    ) {
        this.isDerived = isDerived;
        this.refuml_types = refuml_types;
    }

    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }

    public List<RefUML_Type> getRefuml_types() {
        return refuml_types;
    }

    public void addRefuml_type(Refuml_type refuml_type) {
        this.refuml_types.add(refuml_type);
    }

}
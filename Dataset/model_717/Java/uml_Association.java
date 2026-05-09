





import java.util.List;
import java.util.ArrayList;

public class uml_Association extends Classifier, Relationship {

    private String isDerived;





    private List<uml_Type> uml_types;


    public uml_Association(
        String isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
        this.uml_types = new ArrayList<>();
    }

    public uml_Association(
        String isDerived        ArrayList<uml_Type> uml_types    ) {
        this.isDerived = isDerived;
        this.uml_types = uml_types;
    }

    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }

    public List<uml_Type> getUml_types() {
        return uml_types;
    }

    public void addUml_type(Uml_type uml_type) {
        this.uml_types.add(uml_type);
    }

}
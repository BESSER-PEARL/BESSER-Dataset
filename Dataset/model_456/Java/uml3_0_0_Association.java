





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Association extends Relationship, Classifier {

    private String isDerived;





    private List<uml3_0_0_Type> uml3_0_0_types;


    public uml3_0_0_Association(
        String isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
        this.uml3_0_0_types = new ArrayList<>();
    }

    public uml3_0_0_Association(
        String isDerived        ArrayList<uml3_0_0_Type> uml3_0_0_types    ) {
        this.isDerived = isDerived;
        this.uml3_0_0_types = uml3_0_0_types;
    }

    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }

    public List<uml3_0_0_Type> getUml3_0_0_types() {
        return uml3_0_0_types;
    }

    public void addUml3_0_0_type(Uml3_0_0_type uml3_0_0_type) {
        this.uml3_0_0_types.add(uml3_0_0_type);
    }

}
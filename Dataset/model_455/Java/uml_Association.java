





import java.util.List;
import java.util.ArrayList;

public class uml_Association extends Classifier, Relationship {

    private String isDerived;



    public uml_Association(
        String isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
    }


    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }


}
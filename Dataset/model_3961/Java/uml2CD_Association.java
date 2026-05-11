





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Association extends Classifier, Relationship {

    private boolean isDerived;



    public uml2CD_Association(
        boolean isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
    }


    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }


}
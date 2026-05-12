





import java.util.List;
import java.util.ArrayList;

public class UML2_Association extends Relationship, Classifier {

    private boolean isDerived;



    public UML2_Association(
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
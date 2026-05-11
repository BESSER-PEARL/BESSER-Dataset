





import java.util.List;
import java.util.ArrayList;

public class UML2_Property  {

    private boolean isDerivedUnion;
    private boolean isDerived;



    public UML2_Property(
        boolean isDerivedUnion,        boolean isDerived    ) {
        this.isDerivedUnion = isDerivedUnion;
        this.isDerived = isDerived;
    }


    public boolean getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(boolean isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }
    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }


}
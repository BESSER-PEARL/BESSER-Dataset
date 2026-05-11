





import java.util.List;
import java.util.ArrayList;

public class UML2_Property  {

    private boolean isDerived;
    private boolean isDerivedUnion;



    public UML2_Property(
        boolean isDerived,        boolean isDerivedUnion    ) {
        this.isDerived = isDerived;
        this.isDerivedUnion = isDerivedUnion;
    }


    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }
    public boolean getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(boolean isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }


}
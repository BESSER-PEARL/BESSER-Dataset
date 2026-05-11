





import java.util.List;
import java.util.ArrayList;

public class UML2_Property extends StructuralFeature {

    private boolean isDerivedUnion;



    public UML2_Property(
        boolean isDerivedUnion    ) {
        super(
        );
        this.isDerivedUnion = isDerivedUnion;
    }


    public boolean getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(boolean isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }


}
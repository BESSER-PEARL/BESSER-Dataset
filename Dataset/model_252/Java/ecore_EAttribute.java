





import java.util.List;
import java.util.ArrayList;

public class ecore_EAttribute extends EStructuralFeature {

    private boolean iD;



    public ecore_EAttribute(
        boolean iD    ) {
        super(
        );
        this.iD = iD;
    }


    public boolean getId() {
        return iD;
    }

    public void setId(boolean iD) {
        this.iD = iD;
    }


}
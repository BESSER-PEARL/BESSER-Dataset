





import java.util.List;
import java.util.ArrayList;

public class ecore_EAttribute extends EStructuralFeature {

    private String iD;



    public ecore_EAttribute(
        String iD    ) {
        super(
        );
        this.iD = iD;
    }


    public String getId() {
        return iD;
    }

    public void setId(String iD) {
        this.iD = iD;
    }


}
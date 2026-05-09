





import java.util.List;
import java.util.ArrayList;

public class JTLMM_JTL_Model extends NamedElement {

    private String usedPackage;



    public JTLMM_JTL_Model(
        String usedPackage    ) {
        super(
        );
        this.usedPackage = usedPackage;
    }


    public String getUsedpackage() {
        return usedPackage;
    }

    public void setUsedpackage(String usedPackage) {
        this.usedPackage = usedPackage;
    }


}
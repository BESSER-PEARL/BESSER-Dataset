





import java.util.List;
import java.util.ArrayList;

public class org_structure_Operation extends structure_AbstractOperation, structure_MultiplicityElement {

    private String isAbstract;
    private String uniqueName;



    public org_structure_Operation(
        String isAbstract,        String uniqueName    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uniqueName = uniqueName;
    }


    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getUniquename() {
        return uniqueName;
    }

    public void setUniquename(String uniqueName) {
        this.uniqueName = uniqueName;
    }


}
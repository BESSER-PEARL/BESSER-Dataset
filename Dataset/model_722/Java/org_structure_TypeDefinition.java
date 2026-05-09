





import java.util.List;
import java.util.ArrayList;

public class org_structure_TypeDefinition extends structure_TypeContainer, structure_NamedElement {

    private String isAspect;



    public org_structure_TypeDefinition(
        String isAspect    ) {
        super(
        );
        this.isAspect = isAspect;
    }


    public String getIsaspect() {
        return isAspect;
    }

    public void setIsaspect(String isAspect) {
        this.isAspect = isAspect;
    }


}
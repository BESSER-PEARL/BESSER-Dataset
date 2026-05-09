





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_ClassDefinition extends structure_TypeContainer, structure_GenericTypeDefinition {

    private String isAbstract;



    public kermeta_structure_ClassDefinition(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
    }


    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }


}
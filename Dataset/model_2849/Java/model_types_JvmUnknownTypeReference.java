





import java.util.List;
import java.util.ArrayList;

public class model_types_JvmUnknownTypeReference extends JvmTypeReference {

    private String qualifiedName;



    public model_types_JvmUnknownTypeReference(
        String qualifiedName    ) {
        super(
        );
        this.qualifiedName = qualifiedName;
    }


    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }


}






import java.util.List;
import java.util.ArrayList;

public class types_JvmUnknownTypeReference extends JvmTypeReference {

    private String qualifiedName;



    public types_JvmUnknownTypeReference(
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
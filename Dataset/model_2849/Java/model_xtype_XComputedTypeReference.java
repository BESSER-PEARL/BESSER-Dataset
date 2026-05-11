





import java.util.List;
import java.util.ArrayList;

public class model_xtype_XComputedTypeReference extends JvmSpecializedTypeReference {

    private String typeProvider;



    public model_xtype_XComputedTypeReference(
        String typeProvider    ) {
        super(
        );
        this.typeProvider = typeProvider;
    }


    public String getTypeprovider() {
        return typeProvider;
    }

    public void setTypeprovider(String typeProvider) {
        this.typeProvider = typeProvider;
    }


}
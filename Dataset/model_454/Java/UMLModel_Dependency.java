





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Dependency extends DirectedRelationship, PackageableElement {

    private String supplier;
    private String client;



    public UMLModel_Dependency(
        String supplier,        String client    ) {
        super(
        );
        this.supplier = supplier;
        this.client = client;
    }


    public String getSupplier() {
        return supplier;
    }

    public void setSupplier(String supplier) {
        this.supplier = supplier;
    }
    public String getClient() {
        return client;
    }

    public void setClient(String client) {
        this.client = client;
    }


}
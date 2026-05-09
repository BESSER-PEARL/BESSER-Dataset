





import java.util.List;
import java.util.ArrayList;

public class UMLModel_EncapsulatedClassifier extends StructuredClassifier {

    private String ownedPort;



    public UMLModel_EncapsulatedClassifier(
        String ownedPort    ) {
        super(
        );
        this.ownedPort = ownedPort;
    }


    public String getOwnedport() {
        return ownedPort;
    }

    public void setOwnedport(String ownedPort) {
        this.ownedPort = ownedPort;
    }


}
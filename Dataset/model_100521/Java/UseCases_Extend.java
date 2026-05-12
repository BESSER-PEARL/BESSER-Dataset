





import java.util.List;
import java.util.ArrayList;

public class UseCases_Extend extends RelationShip {






    private List<ExtensionPoint> extensionpoints;


    public UseCases_Extend(
    ) {
        super(
        );
        this.extensionpoints = new ArrayList<>();
    }

    public UseCases_Extend(
        ArrayList<ExtensionPoint> extensionpoints    ) {
        this.extensionpoints = extensionpoints;
    }


    public List<ExtensionPoint> getExtensionpoints() {
        return extensionpoints;
    }

    public void addExtensionpoint(Extensionpoint extensionpoint) {
        this.extensionpoints.add(extensionpoint);
    }

}
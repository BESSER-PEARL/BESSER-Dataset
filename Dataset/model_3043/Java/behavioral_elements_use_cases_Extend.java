





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_use_cases_Extend extends Relationship {






    private List<ExtensionPoint> extensionpoints;


    public behavioral_elements_use_cases_Extend(
    ) {
        super(
        );
        this.extensionpoints = new ArrayList<>();
    }

    public behavioral_elements_use_cases_Extend(
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
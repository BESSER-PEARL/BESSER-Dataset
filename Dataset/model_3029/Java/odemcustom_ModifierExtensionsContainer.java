





import java.util.List;
import java.util.ArrayList;

public class odemcustom_ModifierExtensionsContainer  {






    private List<odemcustom_Extension> odemcustom_extensions;


    public odemcustom_ModifierExtensionsContainer(
    ) {
        this.odemcustom_extensions = new ArrayList<>();
    }

    public odemcustom_ModifierExtensionsContainer(
        ArrayList<odemcustom_Extension> odemcustom_extensions    ) {
        this.odemcustom_extensions = odemcustom_extensions;
    }


    public List<odemcustom_Extension> getOdemcustom_extensions() {
        return odemcustom_extensions;
    }

    public void addOdemcustom_extension(Odemcustom_extension odemcustom_extension) {
        this.odemcustom_extensions.add(odemcustom_extension);
    }

}
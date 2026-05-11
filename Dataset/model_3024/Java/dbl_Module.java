





import java.util.List;
import java.util.ArrayList;

public class dbl_Module extends NamedElement, EmbeddableExtensionsContainer {






    private List<dbl_ExtensionDefinition> dbl_extensiondefinitions;


    public dbl_Module(
    ) {
        super(
        );
        this.dbl_extensiondefinitions = new ArrayList<>();
    }

    public dbl_Module(
        ArrayList<dbl_ExtensionDefinition> dbl_extensiondefinitions    ) {
        this.dbl_extensiondefinitions = dbl_extensiondefinitions;
    }


    public List<dbl_ExtensionDefinition> getDbl_extensiondefinitions() {
        return dbl_extensiondefinitions;
    }

    public void addDbl_extensiondefinition(Dbl_extensiondefinition dbl_extensiondefinition) {
        this.dbl_extensiondefinitions.add(dbl_extensiondefinition);
    }

}






import java.util.List;
import java.util.ArrayList;

public class dbl_Module extends Construct, ConstructiveExtensionAtContentExtensionPoint, NamedElement {






    private List<dbl_Extension> dbl_extensions;




    private List<dbl_ExtensionSemantics> dbl_extensionsemanticss;


    public dbl_Module(
    ) {
        super(
        );
        this.dbl_extensions = new ArrayList<>();
        this.dbl_extensionsemanticss = new ArrayList<>();
    }

    public dbl_Module(
        ArrayList<dbl_Extension> dbl_extensions,        ArrayList<dbl_ExtensionSemantics> dbl_extensionsemanticss    ) {
        this.dbl_extensions = dbl_extensions;
        this.dbl_extensionsemanticss = dbl_extensionsemanticss;
    }


    public List<dbl_Extension> getDbl_extensions() {
        return dbl_extensions;
    }

    public void addDbl_extension(Dbl_extension dbl_extension) {
        this.dbl_extensions.add(dbl_extension);
    }
    public List<dbl_ExtensionSemantics> getDbl_extensionsemanticss() {
        return dbl_extensionsemanticss;
    }

    public void addDbl_extensionsemantics(Dbl_extensionsemantics dbl_extensionsemantics) {
        this.dbl_extensionsemanticss.add(dbl_extensionsemantics);
    }

}
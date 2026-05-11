





import java.util.List;
import java.util.ArrayList;

public class eJSL_ExtensionPackage extends Extension {






    private List<eJSL_Extension> ejsl_extensions;


    public eJSL_ExtensionPackage(
    ) {
        super(
        );
        this.ejsl_extensions = new ArrayList<>();
    }

    public eJSL_ExtensionPackage(
        ArrayList<eJSL_Extension> ejsl_extensions    ) {
        this.ejsl_extensions = ejsl_extensions;
    }


    public List<eJSL_Extension> getEjsl_extensions() {
        return ejsl_extensions;
    }

    public void addEjsl_extension(Ejsl_extension ejsl_extension) {
        this.ejsl_extensions.add(ejsl_extension);
    }

}
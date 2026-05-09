





import java.util.List;
import java.util.ArrayList;

public class spem_MethodConfiguration extends MethodLibraryPackageableElement {






    private List<spem_MethodConfiguration> spem_methodconfigurations;


    public spem_MethodConfiguration(
    ) {
        super(
        );
        this.spem_methodconfigurations = new ArrayList<>();
    }

    public spem_MethodConfiguration(
        ArrayList<spem_MethodConfiguration> spem_methodconfigurations    ) {
        this.spem_methodconfigurations = spem_methodconfigurations;
    }


    public List<spem_MethodConfiguration> getSpem_methodconfigurations() {
        return spem_methodconfigurations;
    }

    public void addSpem_methodconfiguration(Spem_methodconfiguration spem_methodconfiguration) {
        this.spem_methodconfigurations.add(spem_methodconfiguration);
    }

}
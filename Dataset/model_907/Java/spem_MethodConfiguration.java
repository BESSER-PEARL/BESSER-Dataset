





import java.util.List;
import java.util.ArrayList;

public class spem_MethodConfiguration extends MethodLibraryPackageableElement {






    private spem_Activity spem_activity;




    private List<spem_MethodConfiguration> spem_methodconfigurations;




    private spem_Activity spem_activity;


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


    public spem_Activity getSpem_activity() {
        return spem_activity;
    }

    public void setSpem_activity(spem_Activity spem_activity) {
        this.spem_activity = spem_activity;
    }
    public List<spem_MethodConfiguration> getSpem_methodconfigurations() {
        return spem_methodconfigurations;
    }

    public void addSpem_methodconfiguration(Spem_methodconfiguration spem_methodconfiguration) {
        this.spem_methodconfigurations.add(spem_methodconfiguration);
    }
    public spem_Activity getSpem_activity() {
        return spem_activity;
    }

    public void setSpem_activity(spem_Activity spem_activity) {
        this.spem_activity = spem_activity;
    }

}
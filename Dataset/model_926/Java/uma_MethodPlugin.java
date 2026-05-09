





import java.util.List;
import java.util.ArrayList;

public class uma_MethodPlugin extends Package, MethodUnit {

    private String userChangeable;
    private boolean supporting;





    private List<uma_MethodPackage> uma_methodpackages;




    private uma_MethodConfiguration uma_methodconfiguration;




    private uma_MethodPlugin uma_methodplugin;


    public uma_MethodPlugin(
        String userChangeable,        boolean supporting    ) {
        super(
        );
        this.userChangeable = userChangeable;
        this.supporting = supporting;
        this.uma_methodpackages = new ArrayList<>();
    }

    public uma_MethodPlugin(
        String userChangeable,        boolean supporting        ArrayList<uma_MethodPackage> uma_methodpackages    ) {
        this.userChangeable = userChangeable;
        this.supporting = supporting;
        this.uma_methodpackages = uma_methodpackages;
    }

    public String getUserchangeable() {
        return userChangeable;
    }

    public void setUserchangeable(String userChangeable) {
        this.userChangeable = userChangeable;
    }
    public boolean getSupporting() {
        return supporting;
    }

    public void setSupporting(boolean supporting) {
        this.supporting = supporting;
    }

    public List<uma_MethodPackage> getUma_methodpackages() {
        return uma_methodpackages;
    }

    public void addUma_methodpackage(Uma_methodpackage uma_methodpackage) {
        this.uma_methodpackages.add(uma_methodpackage);
    }
    public uma_MethodConfiguration getUma_methodconfiguration() {
        return uma_methodconfiguration;
    }

    public void setUma_methodconfiguration(uma_MethodConfiguration uma_methodconfiguration) {
        this.uma_methodconfiguration = uma_methodconfiguration;
    }
    public uma_MethodPlugin getUma_methodplugin() {
        return uma_methodplugin;
    }

    public void setUma_methodplugin(uma_MethodPlugin uma_methodplugin) {
        this.uma_methodplugin = uma_methodplugin;
    }

}






import java.util.List;
import java.util.ArrayList;

public class uma_MethodPlugin extends Package, MethodUnit {

    private String userChangeable;





    private List<uma_MethodPackage> uma_methodpackages;




    private List<uma_MethodPlugin> uma_methodplugins;


    public uma_MethodPlugin(
        String userChangeable    ) {
        super(
        );
        this.userChangeable = userChangeable;
        this.uma_methodpackages = new ArrayList<>();
        this.uma_methodplugins = new ArrayList<>();
    }

    public uma_MethodPlugin(
        String userChangeable        ArrayList<uma_MethodPackage> uma_methodpackages,        ArrayList<uma_MethodPlugin> uma_methodplugins    ) {
        this.userChangeable = userChangeable;
        this.uma_methodpackages = uma_methodpackages;
        this.uma_methodplugins = uma_methodplugins;
    }

    public String getUserchangeable() {
        return userChangeable;
    }

    public void setUserchangeable(String userChangeable) {
        this.userChangeable = userChangeable;
    }

    public List<uma_MethodPackage> getUma_methodpackages() {
        return uma_methodpackages;
    }

    public void addUma_methodpackage(Uma_methodpackage uma_methodpackage) {
        this.uma_methodpackages.add(uma_methodpackage);
    }
    public List<uma_MethodPlugin> getUma_methodplugins() {
        return uma_methodplugins;
    }

    public void addUma_methodplugin(Uma_methodplugin uma_methodplugin) {
        this.uma_methodplugins.add(uma_methodplugin);
    }

}
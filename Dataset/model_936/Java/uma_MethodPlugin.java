





import java.util.List;
import java.util.ArrayList;

public class uma_MethodPlugin extends MethodUnit {

    private String supporting;
    private String userChangeable;
    private String referencedMethodPlugin;





    private List<uma_MethodPackage> uma_methodpackages;




    private uma_MethodLibrary uma_methodlibrary;


    public uma_MethodPlugin(
        String supporting,        String userChangeable,        String referencedMethodPlugin    ) {
        super(
        );
        this.supporting = supporting;
        this.userChangeable = userChangeable;
        this.referencedMethodPlugin = referencedMethodPlugin;
        this.uma_methodpackages = new ArrayList<>();
    }

    public uma_MethodPlugin(
        String supporting,        String userChangeable,        String referencedMethodPlugin        ArrayList<uma_MethodPackage> uma_methodpackages    ) {
        this.supporting = supporting;
        this.userChangeable = userChangeable;
        this.referencedMethodPlugin = referencedMethodPlugin;
        this.uma_methodpackages = uma_methodpackages;
    }

    public String getSupporting() {
        return supporting;
    }

    public void setSupporting(String supporting) {
        this.supporting = supporting;
    }
    public String getUserchangeable() {
        return userChangeable;
    }

    public void setUserchangeable(String userChangeable) {
        this.userChangeable = userChangeable;
    }
    public String getReferencedmethodplugin() {
        return referencedMethodPlugin;
    }

    public void setReferencedmethodplugin(String referencedMethodPlugin) {
        this.referencedMethodPlugin = referencedMethodPlugin;
    }

    public List<uma_MethodPackage> getUma_methodpackages() {
        return uma_methodpackages;
    }

    public void addUma_methodpackage(Uma_methodpackage uma_methodpackage) {
        this.uma_methodpackages.add(uma_methodpackage);
    }
    public uma_MethodLibrary getUma_methodlibrary() {
        return uma_methodlibrary;
    }

    public void setUma_methodlibrary(uma_MethodLibrary uma_methodlibrary) {
        this.uma_methodlibrary = uma_methodlibrary;
    }

}
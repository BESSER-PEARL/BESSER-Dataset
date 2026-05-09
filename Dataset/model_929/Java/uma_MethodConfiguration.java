





import java.util.List;
import java.util.ArrayList;

public class uma_MethodConfiguration extends MethodUnit {






    private uma_MethodLibrary uma_methodlibrary;




    private List<uma_MethodPackage> uma_methodpackages;




    private uma_ContentCategory uma_contentcategory;




    private List<uma_ContentCategory> uma_contentcategorys;




    private List<uma_MethodConfiguration> uma_methodconfigurations;




    private List<uma_MethodPlugin> uma_methodplugins;


    public uma_MethodConfiguration(
    ) {
        super(
        );
        this.uma_methodpackages = new ArrayList<>();
        this.uma_contentcategorys = new ArrayList<>();
        this.uma_methodconfigurations = new ArrayList<>();
        this.uma_methodplugins = new ArrayList<>();
    }

    public uma_MethodConfiguration(
        ArrayList<uma_MethodPackage> uma_methodpackages,        ArrayList<uma_ContentCategory> uma_contentcategorys,        ArrayList<uma_MethodConfiguration> uma_methodconfigurations,        ArrayList<uma_MethodPlugin> uma_methodplugins    ) {
        this.uma_methodpackages = uma_methodpackages;
        this.uma_contentcategorys = uma_contentcategorys;
        this.uma_methodconfigurations = uma_methodconfigurations;
        this.uma_methodplugins = uma_methodplugins;
    }


    public uma_MethodLibrary getUma_methodlibrary() {
        return uma_methodlibrary;
    }

    public void setUma_methodlibrary(uma_MethodLibrary uma_methodlibrary) {
        this.uma_methodlibrary = uma_methodlibrary;
    }
    public List<uma_MethodPackage> getUma_methodpackages() {
        return uma_methodpackages;
    }

    public void addUma_methodpackage(Uma_methodpackage uma_methodpackage) {
        this.uma_methodpackages.add(uma_methodpackage);
    }
    public uma_ContentCategory getUma_contentcategory() {
        return uma_contentcategory;
    }

    public void setUma_contentcategory(uma_ContentCategory uma_contentcategory) {
        this.uma_contentcategory = uma_contentcategory;
    }
    public List<uma_ContentCategory> getUma_contentcategorys() {
        return uma_contentcategorys;
    }

    public void addUma_contentcategory(Uma_contentcategory uma_contentcategory) {
        this.uma_contentcategorys.add(uma_contentcategory);
    }
    public List<uma_MethodConfiguration> getUma_methodconfigurations() {
        return uma_methodconfigurations;
    }

    public void addUma_methodconfiguration(Uma_methodconfiguration uma_methodconfiguration) {
        this.uma_methodconfigurations.add(uma_methodconfiguration);
    }
    public List<uma_MethodPlugin> getUma_methodplugins() {
        return uma_methodplugins;
    }

    public void addUma_methodplugin(Uma_methodplugin uma_methodplugin) {
        this.uma_methodplugins.add(uma_methodplugin);
    }

}






import java.util.List;
import java.util.ArrayList;

public class uma_MethodConfiguration extends MethodUnit {






    private uma_MethodConfiguration uma_methodconfiguration;




    private List<uma_ContentCategory> uma_contentcategorys;




    private uma_MethodLibrary uma_methodlibrary;




    private List<uma_MethodPackage> uma_methodpackages;




    private uma_ContentCategory uma_contentcategory;




    private List<uma_ContentCategory> uma_contentcategorys;




    private uma_Process uma_process;




    private List<uma_MethodPlugin> uma_methodplugins;




    private uma_Process uma_process;




    private List<uma_ContentCategory> uma_contentcategorys;


    public uma_MethodConfiguration(
    ) {
        super(
        );
        this.uma_contentcategorys = new ArrayList<>();
        this.uma_methodpackages = new ArrayList<>();
        this.uma_contentcategorys = new ArrayList<>();
        this.uma_methodplugins = new ArrayList<>();
        this.uma_contentcategorys = new ArrayList<>();
    }

    public uma_MethodConfiguration(
        ArrayList<uma_ContentCategory> uma_contentcategorys,        ArrayList<uma_MethodPackage> uma_methodpackages,        ArrayList<uma_ContentCategory> uma_contentcategorys,        ArrayList<uma_MethodPlugin> uma_methodplugins,        ArrayList<uma_ContentCategory> uma_contentcategorys    ) {
        this.uma_contentcategorys = uma_contentcategorys;
        this.uma_methodpackages = uma_methodpackages;
        this.uma_contentcategorys = uma_contentcategorys;
        this.uma_methodplugins = uma_methodplugins;
        this.uma_contentcategorys = uma_contentcategorys;
    }


    public uma_MethodConfiguration getUma_methodconfiguration() {
        return uma_methodconfiguration;
    }

    public void setUma_methodconfiguration(uma_MethodConfiguration uma_methodconfiguration) {
        this.uma_methodconfiguration = uma_methodconfiguration;
    }
    public List<uma_ContentCategory> getUma_contentcategorys() {
        return uma_contentcategorys;
    }

    public void addUma_contentcategory(Uma_contentcategory uma_contentcategory) {
        this.uma_contentcategorys.add(uma_contentcategory);
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
    public uma_Process getUma_process() {
        return uma_process;
    }

    public void setUma_process(uma_Process uma_process) {
        this.uma_process = uma_process;
    }
    public List<uma_MethodPlugin> getUma_methodplugins() {
        return uma_methodplugins;
    }

    public void addUma_methodplugin(Uma_methodplugin uma_methodplugin) {
        this.uma_methodplugins.add(uma_methodplugin);
    }
    public uma_Process getUma_process() {
        return uma_process;
    }

    public void setUma_process(uma_Process uma_process) {
        this.uma_process = uma_process;
    }
    public List<uma_ContentCategory> getUma_contentcategorys() {
        return uma_contentcategorys;
    }

    public void addUma_contentcategory(Uma_contentcategory uma_contentcategory) {
        this.uma_contentcategorys.add(uma_contentcategory);
    }

}
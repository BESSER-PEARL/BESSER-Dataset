





import java.util.List;
import java.util.ArrayList;

public class uma_DocumentRoot  {

    private String mixed;





    private List<uma_MethodLibrary> uma_methodlibrarys;




    private List<uma_MethodConfiguration> uma_methodconfigurations;




    private List<uma_MethodPlugin> uma_methodplugins;


    public uma_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.uma_methodlibrarys = new ArrayList<>();
        this.uma_methodconfigurations = new ArrayList<>();
        this.uma_methodplugins = new ArrayList<>();
    }

    public uma_DocumentRoot(
        String mixed        ArrayList<uma_MethodLibrary> uma_methodlibrarys,        ArrayList<uma_MethodConfiguration> uma_methodconfigurations,        ArrayList<uma_MethodPlugin> uma_methodplugins    ) {
        this.mixed = mixed;
        this.uma_methodlibrarys = uma_methodlibrarys;
        this.uma_methodconfigurations = uma_methodconfigurations;
        this.uma_methodplugins = uma_methodplugins;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<uma_MethodLibrary> getUma_methodlibrarys() {
        return uma_methodlibrarys;
    }

    public void addUma_methodlibrary(Uma_methodlibrary uma_methodlibrary) {
        this.uma_methodlibrarys.add(uma_methodlibrary);
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
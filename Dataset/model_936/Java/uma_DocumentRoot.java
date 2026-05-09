





import java.util.List;
import java.util.ArrayList;

public class uma_DocumentRoot  {

    private String mixed;





    private List<uma_MethodPlugin> uma_methodplugins;




    private List<uma_MethodLibrary> uma_methodlibrarys;




    private List<uma_MethodConfiguration> uma_methodconfigurations;


    public uma_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.uma_methodplugins = new ArrayList<>();
        this.uma_methodlibrarys = new ArrayList<>();
        this.uma_methodconfigurations = new ArrayList<>();
    }

    public uma_DocumentRoot(
        String mixed        ArrayList<uma_MethodPlugin> uma_methodplugins,        ArrayList<uma_MethodLibrary> uma_methodlibrarys,        ArrayList<uma_MethodConfiguration> uma_methodconfigurations    ) {
        this.mixed = mixed;
        this.uma_methodplugins = uma_methodplugins;
        this.uma_methodlibrarys = uma_methodlibrarys;
        this.uma_methodconfigurations = uma_methodconfigurations;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<uma_MethodPlugin> getUma_methodplugins() {
        return uma_methodplugins;
    }

    public void addUma_methodplugin(Uma_methodplugin uma_methodplugin) {
        this.uma_methodplugins.add(uma_methodplugin);
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

}
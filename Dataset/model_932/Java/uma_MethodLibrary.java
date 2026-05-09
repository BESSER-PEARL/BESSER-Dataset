





import java.util.List;
import java.util.ArrayList;

public class uma_MethodLibrary extends MethodUnit, Package {






    private List<uma_MethodPlugin> uma_methodplugins;




    private List<uma_MethodConfiguration> uma_methodconfigurations;


    public uma_MethodLibrary(
    ) {
        super(
        );
        this.uma_methodplugins = new ArrayList<>();
        this.uma_methodconfigurations = new ArrayList<>();
    }

    public uma_MethodLibrary(
        ArrayList<uma_MethodPlugin> uma_methodplugins,        ArrayList<uma_MethodConfiguration> uma_methodconfigurations    ) {
        this.uma_methodplugins = uma_methodplugins;
        this.uma_methodconfigurations = uma_methodconfigurations;
    }


    public List<uma_MethodPlugin> getUma_methodplugins() {
        return uma_methodplugins;
    }

    public void addUma_methodplugin(Uma_methodplugin uma_methodplugin) {
        this.uma_methodplugins.add(uma_methodplugin);
    }
    public List<uma_MethodConfiguration> getUma_methodconfigurations() {
        return uma_methodconfigurations;
    }

    public void addUma_methodconfiguration(Uma_methodconfiguration uma_methodconfiguration) {
        this.uma_methodconfigurations.add(uma_methodconfiguration);
    }

}
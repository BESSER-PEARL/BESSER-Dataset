





import java.util.List;
import java.util.ArrayList;

public class uma_MethodPlugin extends Package, MethodUnit {

    private String userChangeable;





    private uma_MethodPlugin uma_methodplugin;




    private uma_MethodConfiguration uma_methodconfiguration;


    public uma_MethodPlugin(
        String userChangeable    ) {
        super(
        );
        this.userChangeable = userChangeable;
    }


    public String getUserchangeable() {
        return userChangeable;
    }

    public void setUserchangeable(String userChangeable) {
        this.userChangeable = userChangeable;
    }

    public uma_MethodPlugin getUma_methodplugin() {
        return uma_methodplugin;
    }

    public void setUma_methodplugin(uma_MethodPlugin uma_methodplugin) {
        this.uma_methodplugin = uma_methodplugin;
    }
    public uma_MethodConfiguration getUma_methodconfiguration() {
        return uma_methodconfiguration;
    }

    public void setUma_methodconfiguration(uma_MethodConfiguration uma_methodconfiguration) {
        this.uma_methodconfiguration = uma_methodconfiguration;
    }

}
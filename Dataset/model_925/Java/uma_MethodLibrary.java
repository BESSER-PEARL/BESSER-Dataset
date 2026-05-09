





import java.util.List;
import java.util.ArrayList;

public class uma_MethodLibrary extends MethodUnit, Package {






    private List<uma_MethodPlugin> uma_methodplugins;


    public uma_MethodLibrary(
    ) {
        super(
        );
        this.uma_methodplugins = new ArrayList<>();
    }

    public uma_MethodLibrary(
        ArrayList<uma_MethodPlugin> uma_methodplugins    ) {
        this.uma_methodplugins = uma_methodplugins;
    }


    public List<uma_MethodPlugin> getUma_methodplugins() {
        return uma_methodplugins;
    }

    public void addUma_methodplugin(Uma_methodplugin uma_methodplugin) {
        this.uma_methodplugins.add(uma_methodplugin);
    }

}
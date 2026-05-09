





import java.util.List;
import java.util.ArrayList;

public class spem_uma_Root  {






    private List<uma_spem_MethodPlugin> uma_spem_methodplugins;


    public spem_uma_Root(
    ) {
        this.uma_spem_methodplugins = new ArrayList<>();
    }

    public spem_uma_Root(
        ArrayList<uma_spem_MethodPlugin> uma_spem_methodplugins    ) {
        this.uma_spem_methodplugins = uma_spem_methodplugins;
    }


    public List<uma_spem_MethodPlugin> getUma_spem_methodplugins() {
        return uma_spem_methodplugins;
    }

    public void addUma_spem_methodplugin(Uma_spem_methodplugin uma_spem_methodplugin) {
        this.uma_spem_methodplugins.add(uma_spem_methodplugin);
    }

}
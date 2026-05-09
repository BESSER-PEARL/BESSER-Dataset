





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__ArquitectureMetamodel  {






    private UnifiedMetamodel__Metamodel unifiedmetamodel__metamodel;




    private List<UnifiedMetamodel__Component> unifiedmetamodel__components;


    public UnifiedMetamodel__ArquitectureMetamodel(
    ) {
        this.unifiedmetamodel__components = new ArrayList<>();
    }

    public UnifiedMetamodel__ArquitectureMetamodel(
        ArrayList<UnifiedMetamodel__Component> unifiedmetamodel__components    ) {
        this.unifiedmetamodel__components = unifiedmetamodel__components;
    }


    public UnifiedMetamodel__Metamodel getUnifiedmetamodel__metamodel() {
        return unifiedmetamodel__metamodel;
    }

    public void setUnifiedmetamodel__metamodel(UnifiedMetamodel__Metamodel unifiedmetamodel__metamodel) {
        this.unifiedmetamodel__metamodel = unifiedmetamodel__metamodel;
    }
    public List<UnifiedMetamodel__Component> getUnifiedmetamodel__components() {
        return unifiedmetamodel__components;
    }

    public void addUnifiedmetamodel__component(Unifiedmetamodel__component unifiedmetamodel__component) {
        this.unifiedmetamodel__components.add(unifiedmetamodel__component);
    }

}
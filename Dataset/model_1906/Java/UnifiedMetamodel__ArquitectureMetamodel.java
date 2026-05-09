





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__ArquitectureMetamodel  {






    private List<UnifiedMetamodel__Component> unifiedmetamodel__components;




    private List<UnifiedMetamodel__RelationArch> unifiedmetamodel__relationarchs;




    private UnifiedMetamodel__Metamodel unifiedmetamodel__metamodel;


    public UnifiedMetamodel__ArquitectureMetamodel(
    ) {
        this.unifiedmetamodel__components = new ArrayList<>();
        this.unifiedmetamodel__relationarchs = new ArrayList<>();
    }

    public UnifiedMetamodel__ArquitectureMetamodel(
        ArrayList<UnifiedMetamodel__Component> unifiedmetamodel__components,        ArrayList<UnifiedMetamodel__RelationArch> unifiedmetamodel__relationarchs    ) {
        this.unifiedmetamodel__components = unifiedmetamodel__components;
        this.unifiedmetamodel__relationarchs = unifiedmetamodel__relationarchs;
    }


    public List<UnifiedMetamodel__Component> getUnifiedmetamodel__components() {
        return unifiedmetamodel__components;
    }

    public void addUnifiedmetamodel__component(Unifiedmetamodel__component unifiedmetamodel__component) {
        this.unifiedmetamodel__components.add(unifiedmetamodel__component);
    }
    public List<UnifiedMetamodel__RelationArch> getUnifiedmetamodel__relationarchs() {
        return unifiedmetamodel__relationarchs;
    }

    public void addUnifiedmetamodel__relationarch(Unifiedmetamodel__relationarch unifiedmetamodel__relationarch) {
        this.unifiedmetamodel__relationarchs.add(unifiedmetamodel__relationarch);
    }
    public UnifiedMetamodel__Metamodel getUnifiedmetamodel__metamodel() {
        return unifiedmetamodel__metamodel;
    }

    public void setUnifiedmetamodel__metamodel(UnifiedMetamodel__Metamodel unifiedmetamodel__metamodel) {
        this.unifiedmetamodel__metamodel = unifiedmetamodel__metamodel;
    }

}
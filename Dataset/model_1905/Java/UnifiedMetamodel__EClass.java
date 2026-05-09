





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__EClass  {

    private String name;





    private UnifiedMetamodel__Annotation unifiedmetamodel__annotation;




    private UnifiedMetamodel__AbstractMethod unifiedmetamodel__abstractmethod;




    private UnifiedMetamodel__Epackage unifiedmetamodel__epackage;




    private UnifiedMetamodel__Attribute unifiedmetamodel__attribute;




    private List<UnifiedMetamodel__Attribute> unifiedmetamodel__attributes;




    private UnifiedMetamodel__AbstractMethod unifiedmetamodel__abstractmethod;


    public UnifiedMetamodel__EClass(
        String name    ) {
        this.name = name;
        this.unifiedmetamodel__attributes = new ArrayList<>();
    }

    public UnifiedMetamodel__EClass(
        String name        ArrayList<UnifiedMetamodel__Attribute> unifiedmetamodel__attributes    ) {
        this.name = name;
        this.unifiedmetamodel__attributes = unifiedmetamodel__attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public UnifiedMetamodel__Annotation getUnifiedmetamodel__annotation() {
        return unifiedmetamodel__annotation;
    }

    public void setUnifiedmetamodel__annotation(UnifiedMetamodel__Annotation unifiedmetamodel__annotation) {
        this.unifiedmetamodel__annotation = unifiedmetamodel__annotation;
    }
    public UnifiedMetamodel__AbstractMethod getUnifiedmetamodel__abstractmethod() {
        return unifiedmetamodel__abstractmethod;
    }

    public void setUnifiedmetamodel__abstractmethod(UnifiedMetamodel__AbstractMethod unifiedmetamodel__abstractmethod) {
        this.unifiedmetamodel__abstractmethod = unifiedmetamodel__abstractmethod;
    }
    public UnifiedMetamodel__Epackage getUnifiedmetamodel__epackage() {
        return unifiedmetamodel__epackage;
    }

    public void setUnifiedmetamodel__epackage(UnifiedMetamodel__Epackage unifiedmetamodel__epackage) {
        this.unifiedmetamodel__epackage = unifiedmetamodel__epackage;
    }
    public UnifiedMetamodel__Attribute getUnifiedmetamodel__attribute() {
        return unifiedmetamodel__attribute;
    }

    public void setUnifiedmetamodel__attribute(UnifiedMetamodel__Attribute unifiedmetamodel__attribute) {
        this.unifiedmetamodel__attribute = unifiedmetamodel__attribute;
    }
    public List<UnifiedMetamodel__Attribute> getUnifiedmetamodel__attributes() {
        return unifiedmetamodel__attributes;
    }

    public void addUnifiedmetamodel__attribute(Unifiedmetamodel__attribute unifiedmetamodel__attribute) {
        this.unifiedmetamodel__attributes.add(unifiedmetamodel__attribute);
    }
    public UnifiedMetamodel__AbstractMethod getUnifiedmetamodel__abstractmethod() {
        return unifiedmetamodel__abstractmethod;
    }

    public void setUnifiedmetamodel__abstractmethod(UnifiedMetamodel__AbstractMethod unifiedmetamodel__abstractmethod) {
        this.unifiedmetamodel__abstractmethod = unifiedmetamodel__abstractmethod;
    }

}
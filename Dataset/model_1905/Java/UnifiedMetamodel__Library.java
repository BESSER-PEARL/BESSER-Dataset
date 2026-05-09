





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Library  {

    private String name;
    private boolean isNative;





    private List<UnifiedMetamodel__Annotation> unifiedmetamodel__annotations;




    private List<UnifiedMetamodel__NativeClass> unifiedmetamodel__nativeclasss;




    private UnifiedMetamodel__Subproject unifiedmetamodel__subproject;


    public UnifiedMetamodel__Library(
        String name,        boolean isNative    ) {
        this.name = name;
        this.isNative = isNative;
        this.unifiedmetamodel__annotations = new ArrayList<>();
        this.unifiedmetamodel__nativeclasss = new ArrayList<>();
    }

    public UnifiedMetamodel__Library(
        String name,        boolean isNative        ArrayList<UnifiedMetamodel__Annotation> unifiedmetamodel__annotations,        ArrayList<UnifiedMetamodel__NativeClass> unifiedmetamodel__nativeclasss    ) {
        this.name = name;
        this.isNative = isNative;
        this.unifiedmetamodel__annotations = unifiedmetamodel__annotations;
        this.unifiedmetamodel__nativeclasss = unifiedmetamodel__nativeclasss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsnative() {
        return isNative;
    }

    public void setIsnative(boolean isNative) {
        this.isNative = isNative;
    }

    public List<UnifiedMetamodel__Annotation> getUnifiedmetamodel__annotations() {
        return unifiedmetamodel__annotations;
    }

    public void addUnifiedmetamodel__annotation(Unifiedmetamodel__annotation unifiedmetamodel__annotation) {
        this.unifiedmetamodel__annotations.add(unifiedmetamodel__annotation);
    }
    public List<UnifiedMetamodel__NativeClass> getUnifiedmetamodel__nativeclasss() {
        return unifiedmetamodel__nativeclasss;
    }

    public void addUnifiedmetamodel__nativeclass(Unifiedmetamodel__nativeclass unifiedmetamodel__nativeclass) {
        this.unifiedmetamodel__nativeclasss.add(unifiedmetamodel__nativeclass);
    }
    public UnifiedMetamodel__Subproject getUnifiedmetamodel__subproject() {
        return unifiedmetamodel__subproject;
    }

    public void setUnifiedmetamodel__subproject(UnifiedMetamodel__Subproject unifiedmetamodel__subproject) {
        this.unifiedmetamodel__subproject = unifiedmetamodel__subproject;
    }

}
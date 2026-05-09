





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Directory  {

    private String purpose;
    private String name;
    private boolean isRoot;





    private UnifiedMetamodel__Functionality unifiedmetamodel__functionality;




    private UnifiedMetamodel__ServicesFront unifiedmetamodel__servicesfront;




    private List<UnifiedMetamodel__Directory> unifiedmetamodel__directorys;




    private UnifiedMetamodel__ComponentFront unifiedmetamodel__componentfront;


    public UnifiedMetamodel__Directory(
        String purpose,        String name,        boolean isRoot    ) {
        this.purpose = purpose;
        this.name = name;
        this.isRoot = isRoot;
        this.unifiedmetamodel__directorys = new ArrayList<>();
    }

    public UnifiedMetamodel__Directory(
        String purpose,        String name,        boolean isRoot        ArrayList<UnifiedMetamodel__Directory> unifiedmetamodel__directorys    ) {
        this.purpose = purpose;
        this.name = name;
        this.isRoot = isRoot;
        this.unifiedmetamodel__directorys = unifiedmetamodel__directorys;
    }

    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsroot() {
        return isRoot;
    }

    public void setIsroot(boolean isRoot) {
        this.isRoot = isRoot;
    }

    public UnifiedMetamodel__Functionality getUnifiedmetamodel__functionality() {
        return unifiedmetamodel__functionality;
    }

    public void setUnifiedmetamodel__functionality(UnifiedMetamodel__Functionality unifiedmetamodel__functionality) {
        this.unifiedmetamodel__functionality = unifiedmetamodel__functionality;
    }
    public UnifiedMetamodel__ServicesFront getUnifiedmetamodel__servicesfront() {
        return unifiedmetamodel__servicesfront;
    }

    public void setUnifiedmetamodel__servicesfront(UnifiedMetamodel__ServicesFront unifiedmetamodel__servicesfront) {
        this.unifiedmetamodel__servicesfront = unifiedmetamodel__servicesfront;
    }
    public List<UnifiedMetamodel__Directory> getUnifiedmetamodel__directorys() {
        return unifiedmetamodel__directorys;
    }

    public void addUnifiedmetamodel__directory(Unifiedmetamodel__directory unifiedmetamodel__directory) {
        this.unifiedmetamodel__directorys.add(unifiedmetamodel__directory);
    }
    public UnifiedMetamodel__ComponentFront getUnifiedmetamodel__componentfront() {
        return unifiedmetamodel__componentfront;
    }

    public void setUnifiedmetamodel__componentfront(UnifiedMetamodel__ComponentFront unifiedmetamodel__componentfront) {
        this.unifiedmetamodel__componentfront = unifiedmetamodel__componentfront;
    }

}
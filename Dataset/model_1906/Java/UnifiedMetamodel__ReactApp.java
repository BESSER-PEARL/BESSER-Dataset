





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__ReactApp  {






    private List<UnifiedMetamodel__ModuleFront> unifiedmetamodel__modulefronts;




    private List<UnifiedMetamodel__Directory> unifiedmetamodel__directorys;




    private UnifiedMetamodel__TechnologyMetamodel unifiedmetamodel__technologymetamodel;




    private List<UnifiedMetamodel__Functionality> unifiedmetamodel__functionalitys;


    public UnifiedMetamodel__ReactApp(
    ) {
        this.unifiedmetamodel__modulefronts = new ArrayList<>();
        this.unifiedmetamodel__directorys = new ArrayList<>();
        this.unifiedmetamodel__functionalitys = new ArrayList<>();
    }

    public UnifiedMetamodel__ReactApp(
        ArrayList<UnifiedMetamodel__ModuleFront> unifiedmetamodel__modulefronts,        ArrayList<UnifiedMetamodel__Directory> unifiedmetamodel__directorys,        ArrayList<UnifiedMetamodel__Functionality> unifiedmetamodel__functionalitys    ) {
        this.unifiedmetamodel__modulefronts = unifiedmetamodel__modulefronts;
        this.unifiedmetamodel__directorys = unifiedmetamodel__directorys;
        this.unifiedmetamodel__functionalitys = unifiedmetamodel__functionalitys;
    }


    public List<UnifiedMetamodel__ModuleFront> getUnifiedmetamodel__modulefronts() {
        return unifiedmetamodel__modulefronts;
    }

    public void addUnifiedmetamodel__modulefront(Unifiedmetamodel__modulefront unifiedmetamodel__modulefront) {
        this.unifiedmetamodel__modulefronts.add(unifiedmetamodel__modulefront);
    }
    public List<UnifiedMetamodel__Directory> getUnifiedmetamodel__directorys() {
        return unifiedmetamodel__directorys;
    }

    public void addUnifiedmetamodel__directory(Unifiedmetamodel__directory unifiedmetamodel__directory) {
        this.unifiedmetamodel__directorys.add(unifiedmetamodel__directory);
    }
    public UnifiedMetamodel__TechnologyMetamodel getUnifiedmetamodel__technologymetamodel() {
        return unifiedmetamodel__technologymetamodel;
    }

    public void setUnifiedmetamodel__technologymetamodel(UnifiedMetamodel__TechnologyMetamodel unifiedmetamodel__technologymetamodel) {
        this.unifiedmetamodel__technologymetamodel = unifiedmetamodel__technologymetamodel;
    }
    public List<UnifiedMetamodel__Functionality> getUnifiedmetamodel__functionalitys() {
        return unifiedmetamodel__functionalitys;
    }

    public void addUnifiedmetamodel__functionality(Unifiedmetamodel__functionality unifiedmetamodel__functionality) {
        this.unifiedmetamodel__functionalitys.add(unifiedmetamodel__functionality);
    }

}
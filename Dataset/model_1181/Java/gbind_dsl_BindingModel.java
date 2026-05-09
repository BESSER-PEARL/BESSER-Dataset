





import java.util.List;
import java.util.ArrayList;

public class gbind_dsl_BindingModel  {

    private String name;





    private List<VirtualMetaclass> virtualmetaclasss;




    private MetamodelDeclaration metamodeldeclaration;




    private BindingOptions bindingoptions;




    private MetamodelDeclaration metamodeldeclaration;


    public gbind_dsl_BindingModel(
        String name    ) {
        this.name = name;
        this.virtualmetaclasss = new ArrayList<>();
    }

    public gbind_dsl_BindingModel(
        String name        ArrayList<VirtualMetaclass> virtualmetaclasss    ) {
        this.name = name;
        this.virtualmetaclasss = virtualmetaclasss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<VirtualMetaclass> getVirtualmetaclasss() {
        return virtualmetaclasss;
    }

    public void addVirtualmetaclass(Virtualmetaclass virtualmetaclass) {
        this.virtualmetaclasss.add(virtualmetaclass);
    }
    public MetamodelDeclaration getMetamodeldeclaration() {
        return metamodeldeclaration;
    }

    public void setMetamodeldeclaration(MetamodelDeclaration metamodeldeclaration) {
        this.metamodeldeclaration = metamodeldeclaration;
    }
    public BindingOptions getBindingoptions() {
        return bindingoptions;
    }

    public void setBindingoptions(BindingOptions bindingoptions) {
        this.bindingoptions = bindingoptions;
    }
    public MetamodelDeclaration getMetamodeldeclaration() {
        return metamodeldeclaration;
    }

    public void setMetamodeldeclaration(MetamodelDeclaration metamodeldeclaration) {
        this.metamodeldeclaration = metamodeldeclaration;
    }

}
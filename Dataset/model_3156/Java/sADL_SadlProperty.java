





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlProperty extends SadlStatement {

    private boolean primaryDeclaration;





    private sADL_SadlResource sadl_sadlresource;




    private sADL_SadlResource sadl_sadlresource;




    private sADL_SadlTypeReference sadl_sadltypereference;




    private sADL_SadlTypeReference sadl_sadltypereference;




    private sADL_SadlClassOrPropertyDeclaration sadl_sadlclassorpropertydeclaration;




    private List<sADL_SadlResource> sadl_sadlresources;


    public sADL_SadlProperty(
        boolean primaryDeclaration    ) {
        super(
        );
        this.primaryDeclaration = primaryDeclaration;
        this.sadl_sadlresources = new ArrayList<>();
    }

    public sADL_SadlProperty(
        boolean primaryDeclaration        ArrayList<sADL_SadlResource> sadl_sadlresources    ) {
        this.primaryDeclaration = primaryDeclaration;
        this.sadl_sadlresources = sadl_sadlresources;
    }

    public boolean getPrimarydeclaration() {
        return primaryDeclaration;
    }

    public void setPrimarydeclaration(boolean primaryDeclaration) {
        this.primaryDeclaration = primaryDeclaration;
    }

    public sADL_SadlResource getSadl_sadlresource() {
        return sadl_sadlresource;
    }

    public void setSadl_sadlresource(sADL_SadlResource sadl_sadlresource) {
        this.sadl_sadlresource = sadl_sadlresource;
    }
    public sADL_SadlResource getSadl_sadlresource() {
        return sadl_sadlresource;
    }

    public void setSadl_sadlresource(sADL_SadlResource sadl_sadlresource) {
        this.sadl_sadlresource = sadl_sadlresource;
    }
    public sADL_SadlTypeReference getSadl_sadltypereference() {
        return sadl_sadltypereference;
    }

    public void setSadl_sadltypereference(sADL_SadlTypeReference sadl_sadltypereference) {
        this.sadl_sadltypereference = sadl_sadltypereference;
    }
    public sADL_SadlTypeReference getSadl_sadltypereference() {
        return sadl_sadltypereference;
    }

    public void setSadl_sadltypereference(sADL_SadlTypeReference sadl_sadltypereference) {
        this.sadl_sadltypereference = sadl_sadltypereference;
    }
    public sADL_SadlClassOrPropertyDeclaration getSadl_sadlclassorpropertydeclaration() {
        return sadl_sadlclassorpropertydeclaration;
    }

    public void setSadl_sadlclassorpropertydeclaration(sADL_SadlClassOrPropertyDeclaration sadl_sadlclassorpropertydeclaration) {
        this.sadl_sadlclassorpropertydeclaration = sadl_sadlclassorpropertydeclaration;
    }
    public List<sADL_SadlResource> getSadl_sadlresources() {
        return sadl_sadlresources;
    }

    public void addSadl_sadlresource(Sadl_sadlresource sadl_sadlresource) {
        this.sadl_sadlresources.add(sadl_sadlresource);
    }

}
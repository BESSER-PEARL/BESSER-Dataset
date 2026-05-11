





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlDifferentFrom extends SadlStatement {

    private boolean complement;





    private List<sADL_SadlClassOrPropertyDeclaration> sadl_sadlclassorpropertydeclarations;




    private sADL_SadlResource sadl_sadlresource;


    public sADL_SadlDifferentFrom(
        boolean complement    ) {
        super(
        );
        this.complement = complement;
        this.sadl_sadlclassorpropertydeclarations = new ArrayList<>();
    }

    public sADL_SadlDifferentFrom(
        boolean complement        ArrayList<sADL_SadlClassOrPropertyDeclaration> sadl_sadlclassorpropertydeclarations    ) {
        this.complement = complement;
        this.sadl_sadlclassorpropertydeclarations = sadl_sadlclassorpropertydeclarations;
    }

    public boolean getComplement() {
        return complement;
    }

    public void setComplement(boolean complement) {
        this.complement = complement;
    }

    public List<sADL_SadlClassOrPropertyDeclaration> getSadl_sadlclassorpropertydeclarations() {
        return sadl_sadlclassorpropertydeclarations;
    }

    public void addSadl_sadlclassorpropertydeclaration(Sadl_sadlclassorpropertydeclaration sadl_sadlclassorpropertydeclaration) {
        this.sadl_sadlclassorpropertydeclarations.add(sadl_sadlclassorpropertydeclaration);
    }
    public sADL_SadlResource getSadl_sadlresource() {
        return sadl_sadlresource;
    }

    public void setSadl_sadlresource(sADL_SadlResource sadl_sadlresource) {
        this.sadl_sadlresource = sadl_sadlresource;
    }

}
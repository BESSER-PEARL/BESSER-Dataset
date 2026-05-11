





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlDisjointClasses extends SadlStatement {






    private List<sADL_SadlClassOrPropertyDeclaration> sadl_sadlclassorpropertydeclarations;




    private List<sADL_SadlResource> sadl_sadlresources;


    public sADL_SadlDisjointClasses(
    ) {
        super(
        );
        this.sadl_sadlclassorpropertydeclarations = new ArrayList<>();
        this.sadl_sadlresources = new ArrayList<>();
    }

    public sADL_SadlDisjointClasses(
        ArrayList<sADL_SadlClassOrPropertyDeclaration> sadl_sadlclassorpropertydeclarations,        ArrayList<sADL_SadlResource> sadl_sadlresources    ) {
        this.sadl_sadlclassorpropertydeclarations = sadl_sadlclassorpropertydeclarations;
        this.sadl_sadlresources = sadl_sadlresources;
    }


    public List<sADL_SadlClassOrPropertyDeclaration> getSadl_sadlclassorpropertydeclarations() {
        return sadl_sadlclassorpropertydeclarations;
    }

    public void addSadl_sadlclassorpropertydeclaration(Sadl_sadlclassorpropertydeclaration sadl_sadlclassorpropertydeclaration) {
        this.sadl_sadlclassorpropertydeclarations.add(sadl_sadlclassorpropertydeclaration);
    }
    public List<sADL_SadlResource> getSadl_sadlresources() {
        return sadl_sadlresources;
    }

    public void addSadl_sadlresource(Sadl_sadlresource sadl_sadlresource) {
        this.sadl_sadlresources.add(sadl_sadlresource);
    }

}
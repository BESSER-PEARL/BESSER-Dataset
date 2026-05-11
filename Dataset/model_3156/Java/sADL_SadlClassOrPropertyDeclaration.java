





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlClassOrPropertyDeclaration extends SadlStatement {






    private List<sADL_SadlResource> sadl_sadlresources;


    public sADL_SadlClassOrPropertyDeclaration(
    ) {
        super(
        );
        this.sadl_sadlresources = new ArrayList<>();
    }

    public sADL_SadlClassOrPropertyDeclaration(
        ArrayList<sADL_SadlResource> sadl_sadlresources    ) {
        this.sadl_sadlresources = sadl_sadlresources;
    }


    public List<sADL_SadlResource> getSadl_sadlresources() {
        return sadl_sadlresources;
    }

    public void addSadl_sadlresource(Sadl_sadlresource sadl_sadlresource) {
        this.sadl_sadlresources.add(sadl_sadlresource);
    }

}
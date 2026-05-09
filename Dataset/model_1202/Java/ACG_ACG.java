





import java.util.List;
import java.util.ArrayList;

public class ACG_ACG extends LocatedElement {

    private String startsWith;
    private String metamodel;



    public ACG_ACG(
        String startsWith,        String metamodel    ) {
        super(
        );
        this.startsWith = startsWith;
        this.metamodel = metamodel;
    }


    public String getStartswith() {
        return startsWith;
    }

    public void setStartswith(String startsWith) {
        this.startsWith = startsWith;
    }
    public String getMetamodel() {
        return metamodel;
    }

    public void setMetamodel(String metamodel) {
        this.metamodel = metamodel;
    }


}
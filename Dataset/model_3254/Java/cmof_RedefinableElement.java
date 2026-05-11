





import java.util.List;
import java.util.ArrayList;

public class cmof_RedefinableElement extends NamedElement {






    private cmof_RedefinableElement cmof_redefinableelement;




    private List<cmof_Classifier> cmof_classifiers;


    public cmof_RedefinableElement(
    ) {
        super(
        );
        this.cmof_classifiers = new ArrayList<>();
    }

    public cmof_RedefinableElement(
        ArrayList<cmof_Classifier> cmof_classifiers    ) {
        this.cmof_classifiers = cmof_classifiers;
    }


    public cmof_RedefinableElement getCmof_redefinableelement() {
        return cmof_redefinableelement;
    }

    public void setCmof_redefinableelement(cmof_RedefinableElement cmof_redefinableelement) {
        this.cmof_redefinableelement = cmof_redefinableelement;
    }
    public List<cmof_Classifier> getCmof_classifiers() {
        return cmof_classifiers;
    }

    public void addCmof_classifier(Cmof_classifier cmof_classifier) {
        this.cmof_classifiers.add(cmof_classifier);
    }

}
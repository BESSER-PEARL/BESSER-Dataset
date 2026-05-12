





import java.util.List;
import java.util.ArrayList;

public class umluseCases_Namespace extends NamedElement {






    private List<umluseCases_PackageableElement> umlusecases_packageableelements;


    public umluseCases_Namespace(
    ) {
        super(
        );
        this.umlusecases_packageableelements = new ArrayList<>();
    }

    public umluseCases_Namespace(
        ArrayList<umluseCases_PackageableElement> umlusecases_packageableelements    ) {
        this.umlusecases_packageableelements = umlusecases_packageableelements;
    }


    public List<umluseCases_PackageableElement> getUmlusecases_packageableelements() {
        return umlusecases_packageableelements;
    }

    public void addUmlusecases_packageableelement(Umlusecases_packageableelement umlusecases_packageableelement) {
        this.umlusecases_packageableelements.add(umlusecases_packageableelement);
    }

}
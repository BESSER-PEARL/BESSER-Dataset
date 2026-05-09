





import java.util.List;
import java.util.ArrayList;

public class imports_StaticMemberImport extends StaticImport {






    private List<ReferenceableElement> referenceableelements;


    public imports_StaticMemberImport(
    ) {
        super(
        );
        this.referenceableelements = new ArrayList<>();
    }

    public imports_StaticMemberImport(
        ArrayList<ReferenceableElement> referenceableelements    ) {
        this.referenceableelements = referenceableelements;
    }


    public List<ReferenceableElement> getReferenceableelements() {
        return referenceableelements;
    }

    public void addReferenceableelement(Referenceableelement referenceableelement) {
        this.referenceableelements.add(referenceableelement);
    }

}
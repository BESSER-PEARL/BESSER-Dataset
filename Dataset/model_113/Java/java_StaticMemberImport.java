





import java.util.List;
import java.util.ArrayList;

public class java_StaticMemberImport extends StaticImport {






    private List<java_ReferenceableElement> java_referenceableelements;


    public java_StaticMemberImport(
    ) {
        super(
        );
        this.java_referenceableelements = new ArrayList<>();
    }

    public java_StaticMemberImport(
        ArrayList<java_ReferenceableElement> java_referenceableelements    ) {
        this.java_referenceableelements = java_referenceableelements;
    }


    public List<java_ReferenceableElement> getJava_referenceableelements() {
        return java_referenceableelements;
    }

    public void addJava_referenceableelement(Java_referenceableelement java_referenceableelement) {
        this.java_referenceableelements.add(java_referenceableelement);
    }

}
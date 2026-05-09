





import java.util.List;
import java.util.ArrayList;

public class JDTAST_Javadoc extends Comment {






    private JDTAST_PackageDeclaration jdtast_packagedeclaration;




    private JDTAST_BodyDeclaration jdtast_bodydeclaration;




    private List<JDTAST_TagElement> jdtast_tagelements;


    public JDTAST_Javadoc(
    ) {
        super(
        );
        this.jdtast_tagelements = new ArrayList<>();
    }

    public JDTAST_Javadoc(
        ArrayList<JDTAST_TagElement> jdtast_tagelements    ) {
        this.jdtast_tagelements = jdtast_tagelements;
    }


    public JDTAST_PackageDeclaration getJdtast_packagedeclaration() {
        return jdtast_packagedeclaration;
    }

    public void setJdtast_packagedeclaration(JDTAST_PackageDeclaration jdtast_packagedeclaration) {
        this.jdtast_packagedeclaration = jdtast_packagedeclaration;
    }
    public JDTAST_BodyDeclaration getJdtast_bodydeclaration() {
        return jdtast_bodydeclaration;
    }

    public void setJdtast_bodydeclaration(JDTAST_BodyDeclaration jdtast_bodydeclaration) {
        this.jdtast_bodydeclaration = jdtast_bodydeclaration;
    }
    public List<JDTAST_TagElement> getJdtast_tagelements() {
        return jdtast_tagelements;
    }

    public void addJdtast_tagelement(Jdtast_tagelement jdtast_tagelement) {
        this.jdtast_tagelements.add(jdtast_tagelement);
    }

}
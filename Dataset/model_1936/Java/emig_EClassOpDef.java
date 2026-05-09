





import java.util.List;
import java.util.ArrayList;

public class emig_EClassOpDef extends OpDef {






    private emig_EPackageOpDef emig_epackageopdef;




    private List<emig_EReferenceOpDef> emig_ereferenceopdefs;


    public emig_EClassOpDef(
    ) {
        super(
        );
        this.emig_ereferenceopdefs = new ArrayList<>();
    }

    public emig_EClassOpDef(
        ArrayList<emig_EReferenceOpDef> emig_ereferenceopdefs    ) {
        this.emig_ereferenceopdefs = emig_ereferenceopdefs;
    }


    public emig_EPackageOpDef getEmig_epackageopdef() {
        return emig_epackageopdef;
    }

    public void setEmig_epackageopdef(emig_EPackageOpDef emig_epackageopdef) {
        this.emig_epackageopdef = emig_epackageopdef;
    }
    public List<emig_EReferenceOpDef> getEmig_ereferenceopdefs() {
        return emig_ereferenceopdefs;
    }

    public void addEmig_ereferenceopdef(Emig_ereferenceopdef emig_ereferenceopdef) {
        this.emig_ereferenceopdefs.add(emig_ereferenceopdef);
    }

}
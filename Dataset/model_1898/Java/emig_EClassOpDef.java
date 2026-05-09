





import java.util.List;
import java.util.ArrayList;

public class emig_EClassOpDef extends OpDef {






    private List<emig_EReferenceOpDef> emig_ereferenceopdefs;




    private emig_EPackageOpDef emig_epackageopdef;




    private List<emig_EAttributeOpDef> emig_eattributeopdefs;


    public emig_EClassOpDef(
    ) {
        super(
        );
        this.emig_ereferenceopdefs = new ArrayList<>();
        this.emig_eattributeopdefs = new ArrayList<>();
    }

    public emig_EClassOpDef(
        ArrayList<emig_EReferenceOpDef> emig_ereferenceopdefs,        ArrayList<emig_EAttributeOpDef> emig_eattributeopdefs    ) {
        this.emig_ereferenceopdefs = emig_ereferenceopdefs;
        this.emig_eattributeopdefs = emig_eattributeopdefs;
    }


    public List<emig_EReferenceOpDef> getEmig_ereferenceopdefs() {
        return emig_ereferenceopdefs;
    }

    public void addEmig_ereferenceopdef(Emig_ereferenceopdef emig_ereferenceopdef) {
        this.emig_ereferenceopdefs.add(emig_ereferenceopdef);
    }
    public emig_EPackageOpDef getEmig_epackageopdef() {
        return emig_epackageopdef;
    }

    public void setEmig_epackageopdef(emig_EPackageOpDef emig_epackageopdef) {
        this.emig_epackageopdef = emig_epackageopdef;
    }
    public List<emig_EAttributeOpDef> getEmig_eattributeopdefs() {
        return emig_eattributeopdefs;
    }

    public void addEmig_eattributeopdef(Emig_eattributeopdef emig_eattributeopdef) {
        this.emig_eattributeopdefs.add(emig_eattributeopdef);
    }

}






import java.util.List;
import java.util.ArrayList;

public class UppaalFlat11_TemplateType  {

    private String declaration;





    private List<UppaalFlat11_LocationType> uppaalflat11_locationtypes;




    private UppaalFlat11_DocumentRoot uppaalflat11_documentroot;




    private UppaalFlat11_InitType uppaalflat11_inittype;


    public UppaalFlat11_TemplateType(
        String declaration    ) {
        this.declaration = declaration;
        this.uppaalflat11_locationtypes = new ArrayList<>();
    }

    public UppaalFlat11_TemplateType(
        String declaration        ArrayList<UppaalFlat11_LocationType> uppaalflat11_locationtypes    ) {
        this.declaration = declaration;
        this.uppaalflat11_locationtypes = uppaalflat11_locationtypes;
    }

    public String getDeclaration() {
        return declaration;
    }

    public void setDeclaration(String declaration) {
        this.declaration = declaration;
    }

    public List<UppaalFlat11_LocationType> getUppaalflat11_locationtypes() {
        return uppaalflat11_locationtypes;
    }

    public void addUppaalflat11_locationtype(Uppaalflat11_locationtype uppaalflat11_locationtype) {
        this.uppaalflat11_locationtypes.add(uppaalflat11_locationtype);
    }
    public UppaalFlat11_DocumentRoot getUppaalflat11_documentroot() {
        return uppaalflat11_documentroot;
    }

    public void setUppaalflat11_documentroot(UppaalFlat11_DocumentRoot uppaalflat11_documentroot) {
        this.uppaalflat11_documentroot = uppaalflat11_documentroot;
    }
    public UppaalFlat11_InitType getUppaalflat11_inittype() {
        return uppaalflat11_inittype;
    }

    public void setUppaalflat11_inittype(UppaalFlat11_InitType uppaalflat11_inittype) {
        this.uppaalflat11_inittype = uppaalflat11_inittype;
    }

}
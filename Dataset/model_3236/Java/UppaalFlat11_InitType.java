





import java.util.List;
import java.util.ArrayList;

public class UppaalFlat11_InitType  {

    private String ref;





    private UppaalFlat11_DocumentRoot uppaalflat11_documentroot;




    private UppaalFlat11_TemplateType uppaalflat11_templatetype;


    public UppaalFlat11_InitType(
        String ref    ) {
        this.ref = ref;
    }


    public String getRef() {
        return ref;
    }

    public void setRef(String ref) {
        this.ref = ref;
    }

    public UppaalFlat11_DocumentRoot getUppaalflat11_documentroot() {
        return uppaalflat11_documentroot;
    }

    public void setUppaalflat11_documentroot(UppaalFlat11_DocumentRoot uppaalflat11_documentroot) {
        this.uppaalflat11_documentroot = uppaalflat11_documentroot;
    }
    public UppaalFlat11_TemplateType getUppaalflat11_templatetype() {
        return uppaalflat11_templatetype;
    }

    public void setUppaalflat11_templatetype(UppaalFlat11_TemplateType uppaalflat11_templatetype) {
        this.uppaalflat11_templatetype = uppaalflat11_templatetype;
    }

}
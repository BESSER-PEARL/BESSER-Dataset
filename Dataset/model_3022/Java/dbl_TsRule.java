





import java.util.List;
import java.util.ArrayList;

public class dbl_TsRule extends NamedElement, ReferableRhsType {

    private String metaClassName;





    private dbl_TextualSyntaxDef dbl_textualsyntaxdef;


    public dbl_TsRule(
        String metaClassName    ) {
        super(
        );
        this.metaClassName = metaClassName;
    }


    public String getMetaclassname() {
        return metaClassName;
    }

    public void setMetaclassname(String metaClassName) {
        this.metaClassName = metaClassName;
    }

    public dbl_TextualSyntaxDef getDbl_textualsyntaxdef() {
        return dbl_textualsyntaxdef;
    }

    public void setDbl_textualsyntaxdef(dbl_TextualSyntaxDef dbl_textualsyntaxdef) {
        this.dbl_textualsyntaxdef = dbl_textualsyntaxdef;
    }

}






import java.util.List;
import java.util.ArrayList;

public class dbl_ExtensionDefinition extends NamedElement {






    private dbl_Mapping dbl_mapping;




    private dbl_TextualSyntaxDef dbl_textualsyntaxdef;




    private dbl_Module dbl_module;


    public dbl_ExtensionDefinition(
    ) {
        super(
        );
    }



    public dbl_Mapping getDbl_mapping() {
        return dbl_mapping;
    }

    public void setDbl_mapping(dbl_Mapping dbl_mapping) {
        this.dbl_mapping = dbl_mapping;
    }
    public dbl_TextualSyntaxDef getDbl_textualsyntaxdef() {
        return dbl_textualsyntaxdef;
    }

    public void setDbl_textualsyntaxdef(dbl_TextualSyntaxDef dbl_textualsyntaxdef) {
        this.dbl_textualsyntaxdef = dbl_textualsyntaxdef;
    }
    public dbl_Module getDbl_module() {
        return dbl_module;
    }

    public void setDbl_module(dbl_Module dbl_module) {
        this.dbl_module = dbl_module;
    }

}






import java.util.List;
import java.util.ArrayList;

public class dbl_ExtensionDefinition extends NamedElement {






    private dbl_Module dbl_module;




    private dbl_TextualSyntaxDef dbl_textualsyntaxdef;




    private List<dbl_Classifier> dbl_classifiers;




    private dbl_Mapping dbl_mapping;


    public dbl_ExtensionDefinition(
    ) {
        super(
        );
        this.dbl_classifiers = new ArrayList<>();
    }

    public dbl_ExtensionDefinition(
        ArrayList<dbl_Classifier> dbl_classifiers    ) {
        this.dbl_classifiers = dbl_classifiers;
    }


    public dbl_Module getDbl_module() {
        return dbl_module;
    }

    public void setDbl_module(dbl_Module dbl_module) {
        this.dbl_module = dbl_module;
    }
    public dbl_TextualSyntaxDef getDbl_textualsyntaxdef() {
        return dbl_textualsyntaxdef;
    }

    public void setDbl_textualsyntaxdef(dbl_TextualSyntaxDef dbl_textualsyntaxdef) {
        this.dbl_textualsyntaxdef = dbl_textualsyntaxdef;
    }
    public List<dbl_Classifier> getDbl_classifiers() {
        return dbl_classifiers;
    }

    public void addDbl_classifier(Dbl_classifier dbl_classifier) {
        this.dbl_classifiers.add(dbl_classifier);
    }
    public dbl_Mapping getDbl_mapping() {
        return dbl_mapping;
    }

    public void setDbl_mapping(dbl_Mapping dbl_mapping) {
        this.dbl_mapping = dbl_mapping;
    }

}
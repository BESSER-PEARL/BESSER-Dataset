





import java.util.List;
import java.util.ArrayList;

public class dbl_TextualSyntaxDef  {






    private dbl_ExtensionRule dbl_extensionrule;




    private List<dbl_TsRule> dbl_tsrules;




    private dbl_ExtensionDefinition dbl_extensiondefinition;


    public dbl_TextualSyntaxDef(
    ) {
        this.dbl_tsrules = new ArrayList<>();
    }

    public dbl_TextualSyntaxDef(
        ArrayList<dbl_TsRule> dbl_tsrules    ) {
        this.dbl_tsrules = dbl_tsrules;
    }


    public dbl_ExtensionRule getDbl_extensionrule() {
        return dbl_extensionrule;
    }

    public void setDbl_extensionrule(dbl_ExtensionRule dbl_extensionrule) {
        this.dbl_extensionrule = dbl_extensionrule;
    }
    public List<dbl_TsRule> getDbl_tsrules() {
        return dbl_tsrules;
    }

    public void addDbl_tsrule(Dbl_tsrule dbl_tsrule) {
        this.dbl_tsrules.add(dbl_tsrule);
    }
    public dbl_ExtensionDefinition getDbl_extensiondefinition() {
        return dbl_extensiondefinition;
    }

    public void setDbl_extensiondefinition(dbl_ExtensionDefinition dbl_extensiondefinition) {
        this.dbl_extensiondefinition = dbl_extensiondefinition;
    }

}
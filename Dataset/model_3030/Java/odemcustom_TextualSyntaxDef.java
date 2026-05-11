





import java.util.List;
import java.util.ArrayList;

public class odemcustom_TextualSyntaxDef  {






    private odemcustom_ExtensionRule odemcustom_extensionrule;




    private List<odemcustom_TsRule> odemcustom_tsrules;




    private odemcustom_ExtensionDefinition odemcustom_extensiondefinition;


    public odemcustom_TextualSyntaxDef(
    ) {
        this.odemcustom_tsrules = new ArrayList<>();
    }

    public odemcustom_TextualSyntaxDef(
        ArrayList<odemcustom_TsRule> odemcustom_tsrules    ) {
        this.odemcustom_tsrules = odemcustom_tsrules;
    }


    public odemcustom_ExtensionRule getOdemcustom_extensionrule() {
        return odemcustom_extensionrule;
    }

    public void setOdemcustom_extensionrule(odemcustom_ExtensionRule odemcustom_extensionrule) {
        this.odemcustom_extensionrule = odemcustom_extensionrule;
    }
    public List<odemcustom_TsRule> getOdemcustom_tsrules() {
        return odemcustom_tsrules;
    }

    public void addOdemcustom_tsrule(Odemcustom_tsrule odemcustom_tsrule) {
        this.odemcustom_tsrules.add(odemcustom_tsrule);
    }
    public odemcustom_ExtensionDefinition getOdemcustom_extensiondefinition() {
        return odemcustom_extensiondefinition;
    }

    public void setOdemcustom_extensiondefinition(odemcustom_ExtensionDefinition odemcustom_extensiondefinition) {
        this.odemcustom_extensiondefinition = odemcustom_extensiondefinition;
    }

}
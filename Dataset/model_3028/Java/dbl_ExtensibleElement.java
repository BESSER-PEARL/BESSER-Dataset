





import java.util.List;
import java.util.ArrayList;

public class dbl_ExtensibleElement extends Construct, NamedElement {

    private boolean instanceOfExtensionDefinition;
    private String concreteSyntax;



    public dbl_ExtensibleElement(
        boolean instanceOfExtensionDefinition,        String concreteSyntax    ) {
        super(
        );
        this.instanceOfExtensionDefinition = instanceOfExtensionDefinition;
        this.concreteSyntax = concreteSyntax;
    }


    public boolean getInstanceofextensiondefinition() {
        return instanceOfExtensionDefinition;
    }

    public void setInstanceofextensiondefinition(boolean instanceOfExtensionDefinition) {
        this.instanceOfExtensionDefinition = instanceOfExtensionDefinition;
    }
    public String getConcretesyntax() {
        return concreteSyntax;
    }

    public void setConcretesyntax(String concreteSyntax) {
        this.concreteSyntax = concreteSyntax;
    }


}
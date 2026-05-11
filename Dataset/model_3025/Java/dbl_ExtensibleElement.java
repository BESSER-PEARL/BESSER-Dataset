





import java.util.List;
import java.util.ArrayList;

public class dbl_ExtensibleElement extends Construct, NamedElement {

    private String concreteSyntax;
    private boolean instanceOfExtensionDefinition;



    public dbl_ExtensibleElement(
        String concreteSyntax,        boolean instanceOfExtensionDefinition    ) {
        super(
        );
        this.concreteSyntax = concreteSyntax;
        this.instanceOfExtensionDefinition = instanceOfExtensionDefinition;
    }


    public String getConcretesyntax() {
        return concreteSyntax;
    }

    public void setConcretesyntax(String concreteSyntax) {
        this.concreteSyntax = concreteSyntax;
    }
    public boolean getInstanceofextensiondefinition() {
        return instanceOfExtensionDefinition;
    }

    public void setInstanceofextensiondefinition(boolean instanceOfExtensionDefinition) {
        this.instanceOfExtensionDefinition = instanceOfExtensionDefinition;
    }


}
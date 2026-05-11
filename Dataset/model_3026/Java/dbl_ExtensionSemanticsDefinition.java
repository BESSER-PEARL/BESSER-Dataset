





import java.util.List;
import java.util.ArrayList;

public class dbl_ExtensionSemanticsDefinition extends LocalScope, ExtensibleElement {






    private dbl_Module dbl_module;




    private dbl_ExtensionDefinition dbl_extensiondefinition;


    public dbl_ExtensionSemanticsDefinition(
    ) {
        super(
        );
    }



    public dbl_Module getDbl_module() {
        return dbl_module;
    }

    public void setDbl_module(dbl_Module dbl_module) {
        this.dbl_module = dbl_module;
    }
    public dbl_ExtensionDefinition getDbl_extensiondefinition() {
        return dbl_extensiondefinition;
    }

    public void setDbl_extensiondefinition(dbl_ExtensionDefinition dbl_extensiondefinition) {
        this.dbl_extensiondefinition = dbl_extensiondefinition;
    }

}
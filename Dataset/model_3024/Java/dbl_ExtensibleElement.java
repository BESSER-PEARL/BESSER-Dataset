





import java.util.List;
import java.util.ArrayList;

public class dbl_ExtensibleElement  {

    private boolean objectIsExtensionInstance;





    private dbl_EmbeddableExtensionsContainer dbl_embeddableextensionscontainer;


    public dbl_ExtensibleElement(
        boolean objectIsExtensionInstance    ) {
        this.objectIsExtensionInstance = objectIsExtensionInstance;
    }


    public boolean getObjectisextensioninstance() {
        return objectIsExtensionInstance;
    }

    public void setObjectisextensioninstance(boolean objectIsExtensionInstance) {
        this.objectIsExtensionInstance = objectIsExtensionInstance;
    }

    public dbl_EmbeddableExtensionsContainer getDbl_embeddableextensionscontainer() {
        return dbl_embeddableextensionscontainer;
    }

    public void setDbl_embeddableextensionscontainer(dbl_EmbeddableExtensionsContainer dbl_embeddableextensionscontainer) {
        this.dbl_embeddableextensionscontainer = dbl_embeddableextensionscontainer;
    }

}






import java.util.List;
import java.util.ArrayList;

public class dbl_ExtensionDefinition extends LanguageConceptClassifier, ExtensibleElement {






    private dbl_Module dbl_module;




    private dbl_Class dbl_class;


    public dbl_ExtensionDefinition(
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
    public dbl_Class getDbl_class() {
        return dbl_class;
    }

    public void setDbl_class(dbl_Class dbl_class) {
        this.dbl_class = dbl_class;
    }

}
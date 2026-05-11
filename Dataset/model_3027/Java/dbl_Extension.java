





import java.util.List;
import java.util.ArrayList;

public class dbl_Extension extends ExtensibleElement, Concept {






    private dbl_SyntaxDefinition dbl_syntaxdefinition;




    private dbl_Concept dbl_concept;


    public dbl_Extension(
    ) {
        super(
        );
    }



    public dbl_SyntaxDefinition getDbl_syntaxdefinition() {
        return dbl_syntaxdefinition;
    }

    public void setDbl_syntaxdefinition(dbl_SyntaxDefinition dbl_syntaxdefinition) {
        this.dbl_syntaxdefinition = dbl_syntaxdefinition;
    }
    public dbl_Concept getDbl_concept() {
        return dbl_concept;
    }

    public void setDbl_concept(dbl_Concept dbl_concept) {
        this.dbl_concept = dbl_concept;
    }

}
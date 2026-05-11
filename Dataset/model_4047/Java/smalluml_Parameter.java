





import java.util.List;
import java.util.ArrayList;

public class smalluml_Parameter extends NamedElement {






    private smalluml_SuperType smalluml_supertype;




    private smalluml_Operation smalluml_operation;


    public smalluml_Parameter(
    ) {
        super(
        );
    }



    public smalluml_SuperType getSmalluml_supertype() {
        return smalluml_supertype;
    }

    public void setSmalluml_supertype(smalluml_SuperType smalluml_supertype) {
        this.smalluml_supertype = smalluml_supertype;
    }
    public smalluml_Operation getSmalluml_operation() {
        return smalluml_operation;
    }

    public void setSmalluml_operation(smalluml_Operation smalluml_operation) {
        this.smalluml_operation = smalluml_operation;
    }

}
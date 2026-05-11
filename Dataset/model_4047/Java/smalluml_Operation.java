





import java.util.List;
import java.util.ArrayList;

public class smalluml_Operation extends NamedElement {

    private boolean isAbstract;





    private smalluml_SuperType smalluml_supertype;


    public smalluml_Operation(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public smalluml_SuperType getSmalluml_supertype() {
        return smalluml_supertype;
    }

    public void setSmalluml_supertype(smalluml_SuperType smalluml_supertype) {
        this.smalluml_supertype = smalluml_supertype;
    }

}
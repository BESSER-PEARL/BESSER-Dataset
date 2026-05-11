





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Generalization extends DirectRelationship {

    private boolean isSubstitutable;



    public uml2CD_Generalization(
        boolean isSubstitutable    ) {
        super(
        );
        this.isSubstitutable = isSubstitutable;
    }


    public boolean getIssubstitutable() {
        return isSubstitutable;
    }

    public void setIssubstitutable(boolean isSubstitutable) {
        this.isSubstitutable = isSubstitutable;
    }


}
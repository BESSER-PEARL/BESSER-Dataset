





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_Generalization extends DirectedRelationship {

    private boolean isSubstitutable;



    public ClassesProv_Generalization(
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
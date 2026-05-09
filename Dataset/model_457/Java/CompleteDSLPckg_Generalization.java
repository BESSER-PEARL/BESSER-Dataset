





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Generalization extends DirectedRelationship {

    private boolean isSubstitutable;



    public CompleteDSLPckg_Generalization(
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
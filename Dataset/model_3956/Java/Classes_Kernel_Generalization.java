





import java.util.List;
import java.util.ArrayList;

public class Classes_Kernel_Generalization extends DirectedRelationship {

    private boolean isSubstitutable;



    public Classes_Kernel_Generalization(
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






import java.util.List;
import java.util.ArrayList;

public class uml_Generalization extends DirectedRelationship {

    private String isSubstitutable;



    public uml_Generalization(
        String isSubstitutable    ) {
        super(
        );
        this.isSubstitutable = isSubstitutable;
    }


    public String getIssubstitutable() {
        return isSubstitutable;
    }

    public void setIssubstitutable(String isSubstitutable) {
        this.isSubstitutable = isSubstitutable;
    }


}
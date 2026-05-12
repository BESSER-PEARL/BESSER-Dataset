





import java.util.List;
import java.util.ArrayList;

public class AsmL_ExistsTerm extends PredicateTerm {

    private String isUnique;



    public AsmL_ExistsTerm(
        String isUnique    ) {
        super(
        );
        this.isUnique = isUnique;
    }


    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
    }


}






import java.util.List;
import java.util.ArrayList;

public class problog_Collection extends Referable {






    private List<problog_Referable> problog_referables;


    public problog_Collection(
    ) {
        super(
        );
        this.problog_referables = new ArrayList<>();
    }

    public problog_Collection(
        ArrayList<problog_Referable> problog_referables    ) {
        this.problog_referables = problog_referables;
    }


    public List<problog_Referable> getProblog_referables() {
        return problog_referables;
    }

    public void addProblog_referable(Problog_referable problog_referable) {
        this.problog_referables.add(problog_referable);
    }

}
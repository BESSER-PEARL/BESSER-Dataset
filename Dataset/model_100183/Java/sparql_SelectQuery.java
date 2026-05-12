





import java.util.List;
import java.util.ArrayList;

public class sparql_SelectQuery extends SelectionQuery {

    private boolean isDistinct;
    private boolean isReduced;
    private boolean all;



    public sparql_SelectQuery(
        boolean isDistinct,        boolean isReduced,        boolean all    ) {
        super(
        );
        this.isDistinct = isDistinct;
        this.isReduced = isReduced;
        this.all = all;
    }


    public boolean getIsdistinct() {
        return isDistinct;
    }

    public void setIsdistinct(boolean isDistinct) {
        this.isDistinct = isDistinct;
    }
    public boolean getIsreduced() {
        return isReduced;
    }

    public void setIsreduced(boolean isReduced) {
        this.isReduced = isReduced;
    }
    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }


}
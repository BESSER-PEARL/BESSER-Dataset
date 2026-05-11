





import java.util.List;
import java.util.ArrayList;

public class majordomo_CompareOperation extends Statement {

    private String comparator;



    public majordomo_CompareOperation(
        String comparator    ) {
        super(
        );
        this.comparator = comparator;
    }


    public String getComparator() {
        return comparator;
    }

    public void setComparator(String comparator) {
        this.comparator = comparator;
    }


}
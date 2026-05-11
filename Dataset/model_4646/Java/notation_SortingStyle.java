





import java.util.List;
import java.util.ArrayList;

public class notation_SortingStyle extends Style {

    private String sortingKeys;
    private String sorting;



    public notation_SortingStyle(
        String sortingKeys,        String sorting    ) {
        super(
        );
        this.sortingKeys = sortingKeys;
        this.sorting = sorting;
    }


    public String getSortingkeys() {
        return sortingKeys;
    }

    public void setSortingkeys(String sortingKeys) {
        this.sortingKeys = sortingKeys;
    }
    public String getSorting() {
        return sorting;
    }

    public void setSorting(String sorting) {
        this.sorting = sorting;
    }


}
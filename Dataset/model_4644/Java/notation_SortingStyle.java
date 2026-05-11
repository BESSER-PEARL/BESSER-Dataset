





import java.util.List;
import java.util.ArrayList;

public class notation_SortingStyle extends Style {

    private String sorting;
    private String sortingKeys;



    public notation_SortingStyle(
        String sorting,        String sortingKeys    ) {
        super(
        );
        this.sorting = sorting;
        this.sortingKeys = sortingKeys;
    }


    public String getSorting() {
        return sorting;
    }

    public void setSorting(String sorting) {
        this.sorting = sorting;
    }
    public String getSortingkeys() {
        return sortingKeys;
    }

    public void setSortingkeys(String sortingKeys) {
        this.sortingKeys = sortingKeys;
    }


}






import java.util.List;
import java.util.ArrayList;

public class notation_FilteringStyle extends Style {

    private String filteringKeys;
    private String filtering;



    public notation_FilteringStyle(
        String filteringKeys,        String filtering    ) {
        super(
        );
        this.filteringKeys = filteringKeys;
        this.filtering = filtering;
    }


    public String getFilteringkeys() {
        return filteringKeys;
    }

    public void setFilteringkeys(String filteringKeys) {
        this.filteringKeys = filteringKeys;
    }
    public String getFiltering() {
        return filtering;
    }

    public void setFiltering(String filtering) {
        this.filtering = filtering;
    }


}
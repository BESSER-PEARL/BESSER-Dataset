





import java.util.List;
import java.util.ArrayList;

public class notation_FilteringStyle extends Style {

    private String filtering;
    private String filteringKeys;



    public notation_FilteringStyle(
        String filtering,        String filteringKeys    ) {
        super(
        );
        this.filtering = filtering;
        this.filteringKeys = filteringKeys;
    }


    public String getFiltering() {
        return filtering;
    }

    public void setFiltering(String filtering) {
        this.filtering = filtering;
    }
    public String getFilteringkeys() {
        return filteringKeys;
    }

    public void setFilteringkeys(String filteringKeys) {
        this.filteringKeys = filteringKeys;
    }


}
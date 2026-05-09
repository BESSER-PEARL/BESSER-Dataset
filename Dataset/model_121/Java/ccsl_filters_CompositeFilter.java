





import java.util.List;
import java.util.ArrayList;

public class ccsl_filters_CompositeFilter extends Filter {

    private String operator;





    private List<filters_Filter> filters_filters;


    public ccsl_filters_CompositeFilter(
        String operator    ) {
        super(
        );
        this.operator = operator;
        this.filters_filters = new ArrayList<>();
    }

    public ccsl_filters_CompositeFilter(
        String operator        ArrayList<filters_Filter> filters_filters    ) {
        this.operator = operator;
        this.filters_filters = filters_filters;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public List<filters_Filter> getFilters_filters() {
        return filters_filters;
    }

    public void addFilters_filter(Filters_filter filters_filter) {
        this.filters_filters.add(filters_filter);
    }

}
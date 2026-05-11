





import java.util.List;
import java.util.ArrayList;

public class extended_FormReport extends FormTypes {

    private String filter;
    private String order;
    private String pagination;



    public extended_FormReport(
        String filter,        String order,        String pagination    ) {
        super(
        );
        this.filter = filter;
        this.order = order;
        this.pagination = pagination;
    }


    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }
    public String getPagination() {
        return pagination;
    }

    public void setPagination(String pagination) {
        this.pagination = pagination;
    }


}
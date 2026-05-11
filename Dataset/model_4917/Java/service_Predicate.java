





import java.util.List;
import java.util.ArrayList;

public class service_Predicate  {






    private service_Selection service_selection;




    private service_Filter service_filter;


    public service_Predicate(
    ) {
    }



    public service_Selection getService_selection() {
        return service_selection;
    }

    public void setService_selection(service_Selection service_selection) {
        this.service_selection = service_selection;
    }
    public service_Filter getService_filter() {
        return service_filter;
    }

    public void setService_filter(service_Filter service_filter) {
        this.service_filter = service_filter;
    }

}
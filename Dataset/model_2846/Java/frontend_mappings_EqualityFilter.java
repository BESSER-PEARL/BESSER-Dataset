





import java.util.List;
import java.util.ArrayList;

public class frontend_mappings_EqualityFilter extends C2CModifier {

    private String filter;



    public frontend_mappings_EqualityFilter(
        String filter    ) {
        super(
        );
        this.filter = filter;
    }


    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }


}
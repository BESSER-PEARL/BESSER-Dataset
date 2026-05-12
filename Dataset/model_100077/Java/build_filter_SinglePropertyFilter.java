





import java.util.List;
import java.util.ArrayList;

public class build_filter_SinglePropertyFilter extends IFilter {

    private String property;



    public build_filter_SinglePropertyFilter(
        String property    ) {
        super(
        );
        this.property = property;
    }


    public String getProperty() {
        return property;
    }

    public void setProperty(String property) {
        this.property = property;
    }


}
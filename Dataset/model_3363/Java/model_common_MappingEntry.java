





import java.util.List;
import java.util.ArrayList;

public class model_common_MappingEntry  {

    private String previous;
    private String current;



    public model_common_MappingEntry(
        String previous,        String current    ) {
        this.previous = previous;
        this.current = current;
    }


    public String getPrevious() {
        return previous;
    }

    public void setPrevious(String previous) {
        this.previous = previous;
    }
    public String getCurrent() {
        return current;
    }

    public void setCurrent(String current) {
        this.current = current;
    }


}






import java.util.List;
import java.util.ArrayList;

public class model_common_MappingEntry  {

    private String current;
    private String previous;



    public model_common_MappingEntry(
        String current,        String previous    ) {
        this.current = current;
        this.previous = previous;
    }


    public String getCurrent() {
        return current;
    }

    public void setCurrent(String current) {
        this.current = current;
    }
    public String getPrevious() {
        return previous;
    }

    public void setPrevious(String previous) {
        this.previous = previous;
    }


}
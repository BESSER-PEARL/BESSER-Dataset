





import java.util.List;
import java.util.ArrayList;

public class build_resolver_IResolver  {

    private String filter;
    private boolean failOnError;



    public build_resolver_IResolver(
        String filter,        boolean failOnError    ) {
        this.filter = filter;
        this.failOnError = failOnError;
    }


    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public boolean getFailonerror() {
        return failOnError;
    }

    public void setFailonerror(boolean failOnError) {
        this.failOnError = failOnError;
    }


}
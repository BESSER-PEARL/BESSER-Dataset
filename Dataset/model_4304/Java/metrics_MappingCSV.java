





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingCSV extends Mapping {

    private String filterPattern;
    private String delimiter;



    public metrics_MappingCSV(
        String filterPattern,        String delimiter    ) {
        super(
        );
        this.filterPattern = filterPattern;
        this.delimiter = delimiter;
    }


    public String getFilterpattern() {
        return filterPattern;
    }

    public void setFilterpattern(String filterPattern) {
        this.filterPattern = filterPattern;
    }
    public String getDelimiter() {
        return delimiter;
    }

    public void setDelimiter(String delimiter) {
        this.delimiter = delimiter;
    }


}
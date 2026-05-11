





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingCSV extends Mapping {

    private String delimiter;
    private String filterPattern;



    public metrics_MappingCSV(
        String delimiter,        String filterPattern    ) {
        super(
        );
        this.delimiter = delimiter;
        this.filterPattern = filterPattern;
    }


    public String getDelimiter() {
        return delimiter;
    }

    public void setDelimiter(String delimiter) {
        this.delimiter = delimiter;
    }
    public String getFilterpattern() {
        return filterPattern;
    }

    public void setFilterpattern(String filterPattern) {
        this.filterPattern = filterPattern;
    }


}






import java.util.List;
import java.util.ArrayList;

public class metrics_MappingXLS extends Mapping {

    private String filterPattern;
    private String sheetNumber;



    public metrics_MappingXLS(
        String filterPattern,        String sheetNumber    ) {
        super(
        );
        this.filterPattern = filterPattern;
        this.sheetNumber = sheetNumber;
    }


    public String getFilterpattern() {
        return filterPattern;
    }

    public void setFilterpattern(String filterPattern) {
        this.filterPattern = filterPattern;
    }
    public String getSheetnumber() {
        return sheetNumber;
    }

    public void setSheetnumber(String sheetNumber) {
        this.sheetNumber = sheetNumber;
    }


}
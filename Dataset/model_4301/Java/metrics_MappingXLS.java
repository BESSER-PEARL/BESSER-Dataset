





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingXLS extends Mapping {

    private String sheetNumber;
    private String filterPattern;



    public metrics_MappingXLS(
        String sheetNumber,        String filterPattern    ) {
        super(
        );
        this.sheetNumber = sheetNumber;
        this.filterPattern = filterPattern;
    }


    public String getSheetnumber() {
        return sheetNumber;
    }

    public void setSheetnumber(String sheetNumber) {
        this.sheetNumber = sheetNumber;
    }
    public String getFilterpattern() {
        return filterPattern;
    }

    public void setFilterpattern(String filterPattern) {
        this.filterPattern = filterPattern;
    }


}






import java.util.List;
import java.util.ArrayList;

public class metrics_MappingXLS extends Mapping {

    private String columnHeaders;
    private String firstDataRow;
    private String headerRow;
    private String sheetNumber;





    private List<metrics_DataKind> metrics_datakinds;


    public metrics_MappingXLS(
        String columnHeaders,        String firstDataRow,        String headerRow,        String sheetNumber    ) {
        super(
        );
        this.columnHeaders = columnHeaders;
        this.firstDataRow = firstDataRow;
        this.headerRow = headerRow;
        this.sheetNumber = sheetNumber;
        this.metrics_datakinds = new ArrayList<>();
    }

    public metrics_MappingXLS(
        String columnHeaders,        String firstDataRow,        String headerRow,        String sheetNumber        ArrayList<metrics_DataKind> metrics_datakinds    ) {
        this.columnHeaders = columnHeaders;
        this.firstDataRow = firstDataRow;
        this.headerRow = headerRow;
        this.sheetNumber = sheetNumber;
        this.metrics_datakinds = metrics_datakinds;
    }

    public String getColumnheaders() {
        return columnHeaders;
    }

    public void setColumnheaders(String columnHeaders) {
        this.columnHeaders = columnHeaders;
    }
    public String getFirstdatarow() {
        return firstDataRow;
    }

    public void setFirstdatarow(String firstDataRow) {
        this.firstDataRow = firstDataRow;
    }
    public String getHeaderrow() {
        return headerRow;
    }

    public void setHeaderrow(String headerRow) {
        this.headerRow = headerRow;
    }
    public String getSheetnumber() {
        return sheetNumber;
    }

    public void setSheetnumber(String sheetNumber) {
        this.sheetNumber = sheetNumber;
    }

    public List<metrics_DataKind> getMetrics_datakinds() {
        return metrics_datakinds;
    }

    public void addMetrics_datakind(Metrics_datakind metrics_datakind) {
        this.metrics_datakinds.add(metrics_datakind);
    }

}
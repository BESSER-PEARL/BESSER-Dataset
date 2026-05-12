





import java.util.List;
import java.util.ArrayList;

public class connection_EDIFACTColumn extends MetadataColumn {

    private String EDIColumnName;
    private String EDIXpath;



    public connection_EDIFACTColumn(
        String EDIColumnName,        String EDIXpath    ) {
        super(
        );
        this.EDIColumnName = EDIColumnName;
        this.EDIXpath = EDIXpath;
    }


    public String getEdicolumnname() {
        return EDIColumnName;
    }

    public void setEdicolumnname(String EDIColumnName) {
        this.EDIColumnName = EDIColumnName;
    }
    public String getEdixpath() {
        return EDIXpath;
    }

    public void setEdixpath(String EDIXpath) {
        this.EDIXpath = EDIXpath;
    }


}
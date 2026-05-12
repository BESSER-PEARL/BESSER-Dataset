





import java.util.List;
import java.util.ArrayList;

public class connection_EDIFACTColumn extends MetadataColumn {

    private String EDIXpath;
    private String EDIColumnName;



    public connection_EDIFACTColumn(
        String EDIXpath,        String EDIColumnName    ) {
        super(
        );
        this.EDIXpath = EDIXpath;
        this.EDIColumnName = EDIColumnName;
    }


    public String getEdixpath() {
        return EDIXpath;
    }

    public void setEdixpath(String EDIXpath) {
        this.EDIXpath = EDIXpath;
    }
    public String getEdicolumnname() {
        return EDIColumnName;
    }

    public void setEdicolumnname(String EDIColumnName) {
        this.EDIColumnName = EDIColumnName;
    }


}
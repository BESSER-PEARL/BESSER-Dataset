





import java.util.List;
import java.util.ArrayList;

public class connection_MetadataTable  {

    private String tableType;
    private boolean activatedCDC;
    private String sourceName;
    private boolean attachedCDC;





    private connection_SAPFunctionUnit connection_sapfunctionunit;




    private connection_SAPFunctionUnit connection_sapfunctionunit;




    private connection_MetadataColumn connection_metadatacolumn;




    private connection_Connection connection_connection;




    private List<connection_MetadataColumn> connection_metadatacolumns;


    public connection_MetadataTable(
        String tableType,        boolean activatedCDC,        String sourceName,        boolean attachedCDC    ) {
        this.tableType = tableType;
        this.activatedCDC = activatedCDC;
        this.sourceName = sourceName;
        this.attachedCDC = attachedCDC;
        this.connection_metadatacolumns = new ArrayList<>();
    }

    public connection_MetadataTable(
        String tableType,        boolean activatedCDC,        String sourceName,        boolean attachedCDC        ArrayList<connection_MetadataColumn> connection_metadatacolumns    ) {
        this.tableType = tableType;
        this.activatedCDC = activatedCDC;
        this.sourceName = sourceName;
        this.attachedCDC = attachedCDC;
        this.connection_metadatacolumns = connection_metadatacolumns;
    }

    public String getTabletype() {
        return tableType;
    }

    public void setTabletype(String tableType) {
        this.tableType = tableType;
    }
    public boolean getActivatedcdc() {
        return activatedCDC;
    }

    public void setActivatedcdc(boolean activatedCDC) {
        this.activatedCDC = activatedCDC;
    }
    public String getSourcename() {
        return sourceName;
    }

    public void setSourcename(String sourceName) {
        this.sourceName = sourceName;
    }
    public boolean getAttachedcdc() {
        return attachedCDC;
    }

    public void setAttachedcdc(boolean attachedCDC) {
        this.attachedCDC = attachedCDC;
    }

    public connection_SAPFunctionUnit getConnection_sapfunctionunit() {
        return connection_sapfunctionunit;
    }

    public void setConnection_sapfunctionunit(connection_SAPFunctionUnit connection_sapfunctionunit) {
        this.connection_sapfunctionunit = connection_sapfunctionunit;
    }
    public connection_SAPFunctionUnit getConnection_sapfunctionunit() {
        return connection_sapfunctionunit;
    }

    public void setConnection_sapfunctionunit(connection_SAPFunctionUnit connection_sapfunctionunit) {
        this.connection_sapfunctionunit = connection_sapfunctionunit;
    }
    public connection_MetadataColumn getConnection_metadatacolumn() {
        return connection_metadatacolumn;
    }

    public void setConnection_metadatacolumn(connection_MetadataColumn connection_metadatacolumn) {
        this.connection_metadatacolumn = connection_metadatacolumn;
    }
    public connection_Connection getConnection_connection() {
        return connection_connection;
    }

    public void setConnection_connection(connection_Connection connection_connection) {
        this.connection_connection = connection_connection;
    }
    public List<connection_MetadataColumn> getConnection_metadatacolumns() {
        return connection_metadatacolumns;
    }

    public void addConnection_metadatacolumn(Connection_metadatacolumn connection_metadatacolumn) {
        this.connection_metadatacolumns.add(connection_metadatacolumn);
    }

}
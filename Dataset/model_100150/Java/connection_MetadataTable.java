





import java.util.List;
import java.util.ArrayList;

public class connection_MetadataTable extends AbstractMetadataObject {

    private String sourceName;
    private String tableType;
    private boolean activatedCDC;
    private boolean attachedCDC;





    private List<connection_MetadataColumn> connection_metadatacolumns;




    private connection_Connection connection_connection;




    private connection_Connection connection_connection;




    private connection_MetadataColumn connection_metadatacolumn;


    public connection_MetadataTable(
        String sourceName,        String tableType,        boolean activatedCDC,        boolean attachedCDC    ) {
        super(
        );
        this.sourceName = sourceName;
        this.tableType = tableType;
        this.activatedCDC = activatedCDC;
        this.attachedCDC = attachedCDC;
        this.connection_metadatacolumns = new ArrayList<>();
    }

    public connection_MetadataTable(
        String sourceName,        String tableType,        boolean activatedCDC,        boolean attachedCDC        ArrayList<connection_MetadataColumn> connection_metadatacolumns    ) {
        this.sourceName = sourceName;
        this.tableType = tableType;
        this.activatedCDC = activatedCDC;
        this.attachedCDC = attachedCDC;
        this.connection_metadatacolumns = connection_metadatacolumns;
    }

    public String getSourcename() {
        return sourceName;
    }

    public void setSourcename(String sourceName) {
        this.sourceName = sourceName;
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
    public boolean getAttachedcdc() {
        return attachedCDC;
    }

    public void setAttachedcdc(boolean attachedCDC) {
        this.attachedCDC = attachedCDC;
    }

    public List<connection_MetadataColumn> getConnection_metadatacolumns() {
        return connection_metadatacolumns;
    }

    public void addConnection_metadatacolumn(Connection_metadatacolumn connection_metadatacolumn) {
        this.connection_metadatacolumns.add(connection_metadatacolumn);
    }
    public connection_Connection getConnection_connection() {
        return connection_connection;
    }

    public void setConnection_connection(connection_Connection connection_connection) {
        this.connection_connection = connection_connection;
    }
    public connection_Connection getConnection_connection() {
        return connection_connection;
    }

    public void setConnection_connection(connection_Connection connection_connection) {
        this.connection_connection = connection_connection;
    }
    public connection_MetadataColumn getConnection_metadatacolumn() {
        return connection_metadatacolumn;
    }

    public void setConnection_metadatacolumn(connection_MetadataColumn connection_metadatacolumn) {
        this.connection_metadatacolumn = connection_metadatacolumn;
    }

}
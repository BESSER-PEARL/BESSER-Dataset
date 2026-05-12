





import java.util.List;
import java.util.ArrayList;

public class connection_MetadataTable extends AbstractMetadataObject {

    private boolean activatedCDC;
    private String tableType;
    private String sourceName;
    private boolean attachedCDC;





    private connection_Connection connection_connection;




    private connection_Connection connection_connection;


    public connection_MetadataTable(
        boolean activatedCDC,        String tableType,        String sourceName,        boolean attachedCDC    ) {
        super(
        );
        this.activatedCDC = activatedCDC;
        this.tableType = tableType;
        this.sourceName = sourceName;
        this.attachedCDC = attachedCDC;
    }


    public boolean getActivatedcdc() {
        return activatedCDC;
    }

    public void setActivatedcdc(boolean activatedCDC) {
        this.activatedCDC = activatedCDC;
    }
    public String getTabletype() {
        return tableType;
    }

    public void setTabletype(String tableType) {
        this.tableType = tableType;
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

}
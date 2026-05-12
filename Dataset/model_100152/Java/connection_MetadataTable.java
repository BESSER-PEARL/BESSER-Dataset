





import java.util.List;
import java.util.ArrayList;

public class connection_MetadataTable extends core_Class, AbstractMetadataObject {

    private String sourceName;
    private boolean activatedCDC;
    private String tableType;
    private boolean attachedCDC;





    private List<connection_MetadataColumn> connection_metadatacolumns;




    private connection_MetadataColumn connection_metadatacolumn;


    public connection_MetadataTable(
        String sourceName,        boolean activatedCDC,        String tableType,        boolean attachedCDC    ) {
        super(
        );
        this.sourceName = sourceName;
        this.activatedCDC = activatedCDC;
        this.tableType = tableType;
        this.attachedCDC = attachedCDC;
        this.connection_metadatacolumns = new ArrayList<>();
    }

    public connection_MetadataTable(
        String sourceName,        boolean activatedCDC,        String tableType,        boolean attachedCDC        ArrayList<connection_MetadataColumn> connection_metadatacolumns    ) {
        this.sourceName = sourceName;
        this.activatedCDC = activatedCDC;
        this.tableType = tableType;
        this.attachedCDC = attachedCDC;
        this.connection_metadatacolumns = connection_metadatacolumns;
    }

    public String getSourcename() {
        return sourceName;
    }

    public void setSourcename(String sourceName) {
        this.sourceName = sourceName;
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
    public connection_MetadataColumn getConnection_metadatacolumn() {
        return connection_metadatacolumn;
    }

    public void setConnection_metadatacolumn(connection_MetadataColumn connection_metadatacolumn) {
        this.connection_metadatacolumn = connection_metadatacolumn;
    }

}
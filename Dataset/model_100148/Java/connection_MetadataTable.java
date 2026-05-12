





import java.util.List;
import java.util.ArrayList;

public class connection_MetadataTable extends AbstractMetadataObject, core_Class {

    private boolean attachedCDC;
    private String tableType;
    private String sourceName;
    private boolean activatedCDC;





    private connection_SAPFunctionUnit connection_sapfunctionunit;




    private connection_SAPFunctionUnit connection_sapfunctionunit;




    private connection_SalesforceModuleUnit connection_salesforcemoduleunit;




    private connection_Connection connection_connection;




    private connection_SalesforceModuleUnit connection_salesforcemoduleunit;


    public connection_MetadataTable(
        boolean attachedCDC,        String tableType,        String sourceName,        boolean activatedCDC    ) {
        super(
        );
        this.attachedCDC = attachedCDC;
        this.tableType = tableType;
        this.sourceName = sourceName;
        this.activatedCDC = activatedCDC;
    }


    public boolean getAttachedcdc() {
        return attachedCDC;
    }

    public void setAttachedcdc(boolean attachedCDC) {
        this.attachedCDC = attachedCDC;
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
    public boolean getActivatedcdc() {
        return activatedCDC;
    }

    public void setActivatedcdc(boolean activatedCDC) {
        this.activatedCDC = activatedCDC;
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
    public connection_SalesforceModuleUnit getConnection_salesforcemoduleunit() {
        return connection_salesforcemoduleunit;
    }

    public void setConnection_salesforcemoduleunit(connection_SalesforceModuleUnit connection_salesforcemoduleunit) {
        this.connection_salesforcemoduleunit = connection_salesforcemoduleunit;
    }
    public connection_Connection getConnection_connection() {
        return connection_connection;
    }

    public void setConnection_connection(connection_Connection connection_connection) {
        this.connection_connection = connection_connection;
    }
    public connection_SalesforceModuleUnit getConnection_salesforcemoduleunit() {
        return connection_salesforcemoduleunit;
    }

    public void setConnection_salesforcemoduleunit(connection_SalesforceModuleUnit connection_salesforcemoduleunit) {
        this.connection_salesforcemoduleunit = connection_salesforcemoduleunit;
    }

}
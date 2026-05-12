





import java.util.List;
import java.util.ArrayList;

public class connection_SAPFunctionUnit extends AbstractMetadataObject {

    private String OutputType;
    private String OutputTableName;
    private String Document;
    private String Name;





    private connection_MetadataTable connection_metadatatable;




    private List<connection_MetadataTable> connection_metadatatables;


    public connection_SAPFunctionUnit(
        String OutputType,        String OutputTableName,        String Document,        String Name    ) {
        super(
        );
        this.OutputType = OutputType;
        this.OutputTableName = OutputTableName;
        this.Document = Document;
        this.Name = Name;
        this.connection_metadatatables = new ArrayList<>();
    }

    public connection_SAPFunctionUnit(
        String OutputType,        String OutputTableName,        String Document,        String Name        ArrayList<connection_MetadataTable> connection_metadatatables    ) {
        this.OutputType = OutputType;
        this.OutputTableName = OutputTableName;
        this.Document = Document;
        this.Name = Name;
        this.connection_metadatatables = connection_metadatatables;
    }

    public String getOutputtype() {
        return OutputType;
    }

    public void setOutputtype(String OutputType) {
        this.OutputType = OutputType;
    }
    public String getOutputtablename() {
        return OutputTableName;
    }

    public void setOutputtablename(String OutputTableName) {
        this.OutputTableName = OutputTableName;
    }
    public String getDocument() {
        return Document;
    }

    public void setDocument(String Document) {
        this.Document = Document;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public connection_MetadataTable getConnection_metadatatable() {
        return connection_metadatatable;
    }

    public void setConnection_metadatatable(connection_MetadataTable connection_metadatatable) {
        this.connection_metadatatable = connection_metadatatable;
    }
    public List<connection_MetadataTable> getConnection_metadatatables() {
        return connection_metadatatables;
    }

    public void addConnection_metadatatable(Connection_metadatatable connection_metadatatable) {
        this.connection_metadatatables.add(connection_metadatatable);
    }

}
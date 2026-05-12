





import java.util.List;
import java.util.ArrayList;

public class connection_SAPFunctionUnit extends AbstractMetadataObject {

    private String Name;
    private String OutputTableName;
    private String OutputType;
    private String Document;





    private List<connection_MetadataTable> connection_metadatatables;




    private connection_MetadataTable connection_metadatatable;


    public connection_SAPFunctionUnit(
        String Name,        String OutputTableName,        String OutputType,        String Document    ) {
        super(
        );
        this.Name = Name;
        this.OutputTableName = OutputTableName;
        this.OutputType = OutputType;
        this.Document = Document;
        this.connection_metadatatables = new ArrayList<>();
    }

    public connection_SAPFunctionUnit(
        String Name,        String OutputTableName,        String OutputType,        String Document        ArrayList<connection_MetadataTable> connection_metadatatables    ) {
        this.Name = Name;
        this.OutputTableName = OutputTableName;
        this.OutputType = OutputType;
        this.Document = Document;
        this.connection_metadatatables = connection_metadatatables;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getOutputtablename() {
        return OutputTableName;
    }

    public void setOutputtablename(String OutputTableName) {
        this.OutputTableName = OutputTableName;
    }
    public String getOutputtype() {
        return OutputType;
    }

    public void setOutputtype(String OutputType) {
        this.OutputType = OutputType;
    }
    public String getDocument() {
        return Document;
    }

    public void setDocument(String Document) {
        this.Document = Document;
    }

    public List<connection_MetadataTable> getConnection_metadatatables() {
        return connection_metadatatables;
    }

    public void addConnection_metadatatable(Connection_metadatatable connection_metadatatable) {
        this.connection_metadatatables.add(connection_metadatatable);
    }
    public connection_MetadataTable getConnection_metadatatable() {
        return connection_metadatatable;
    }

    public void setConnection_metadatatable(connection_MetadataTable connection_metadatatable) {
        this.connection_metadatatable = connection_metadatatable;
    }

}
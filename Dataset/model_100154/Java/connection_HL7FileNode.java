





import java.util.List;
import java.util.ArrayList;

public class connection_HL7FileNode  {

    private boolean Repeatable;
    private String RelatedColumn;
    private String Attribute;
    private int Order;
    private String FilePath;
    private String DefaultValue;





    private connection_HL7Connection connection_hl7connection;


    public connection_HL7FileNode(
        boolean Repeatable,        String RelatedColumn,        String Attribute,        int Order,        String FilePath,        String DefaultValue    ) {
        this.Repeatable = Repeatable;
        this.RelatedColumn = RelatedColumn;
        this.Attribute = Attribute;
        this.Order = Order;
        this.FilePath = FilePath;
        this.DefaultValue = DefaultValue;
    }


    public boolean getRepeatable() {
        return Repeatable;
    }

    public void setRepeatable(boolean Repeatable) {
        this.Repeatable = Repeatable;
    }
    public String getRelatedcolumn() {
        return RelatedColumn;
    }

    public void setRelatedcolumn(String RelatedColumn) {
        this.RelatedColumn = RelatedColumn;
    }
    public String getAttribute() {
        return Attribute;
    }

    public void setAttribute(String Attribute) {
        this.Attribute = Attribute;
    }
    public int getOrder() {
        return Order;
    }

    public void setOrder(int Order) {
        this.Order = Order;
    }
    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
    }
    public String getDefaultvalue() {
        return DefaultValue;
    }

    public void setDefaultvalue(String DefaultValue) {
        this.DefaultValue = DefaultValue;
    }

    public connection_HL7Connection getConnection_hl7connection() {
        return connection_hl7connection;
    }

    public void setConnection_hl7connection(connection_HL7Connection connection_hl7connection) {
        this.connection_hl7connection = connection_hl7connection;
    }

}
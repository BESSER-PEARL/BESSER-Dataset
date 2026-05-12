





import java.util.List;
import java.util.ArrayList;

public class connection_HL7FileNode  {

    private String FilePath;
    private String DefaultValue;
    private int Order;
    private String RelatedColumn;
    private String Attribute;
    private boolean Repeatable;





    private connection_HL7Connection connection_hl7connection;


    public connection_HL7FileNode(
        String FilePath,        String DefaultValue,        int Order,        String RelatedColumn,        String Attribute,        boolean Repeatable    ) {
        this.FilePath = FilePath;
        this.DefaultValue = DefaultValue;
        this.Order = Order;
        this.RelatedColumn = RelatedColumn;
        this.Attribute = Attribute;
        this.Repeatable = Repeatable;
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
    public int getOrder() {
        return Order;
    }

    public void setOrder(int Order) {
        this.Order = Order;
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
    public boolean getRepeatable() {
        return Repeatable;
    }

    public void setRepeatable(boolean Repeatable) {
        this.Repeatable = Repeatable;
    }

    public connection_HL7Connection getConnection_hl7connection() {
        return connection_hl7connection;
    }

    public void setConnection_hl7connection(connection_HL7Connection connection_hl7connection) {
        this.connection_hl7connection = connection_hl7connection;
    }

}
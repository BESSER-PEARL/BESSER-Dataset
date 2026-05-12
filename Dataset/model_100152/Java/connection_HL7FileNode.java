





import java.util.List;
import java.util.ArrayList;

public class connection_HL7FileNode  {

    private String RelatedColumn;
    private int Order;
    private String Attribute;
    private String DefaultValue;
    private String FilePath;
    private boolean Repeatable;





    private connection_HL7Connection connection_hl7connection;


    public connection_HL7FileNode(
        String RelatedColumn,        int Order,        String Attribute,        String DefaultValue,        String FilePath,        boolean Repeatable    ) {
        this.RelatedColumn = RelatedColumn;
        this.Order = Order;
        this.Attribute = Attribute;
        this.DefaultValue = DefaultValue;
        this.FilePath = FilePath;
        this.Repeatable = Repeatable;
    }


    public String getRelatedcolumn() {
        return RelatedColumn;
    }

    public void setRelatedcolumn(String RelatedColumn) {
        this.RelatedColumn = RelatedColumn;
    }
    public int getOrder() {
        return Order;
    }

    public void setOrder(int Order) {
        this.Order = Order;
    }
    public String getAttribute() {
        return Attribute;
    }

    public void setAttribute(String Attribute) {
        this.Attribute = Attribute;
    }
    public String getDefaultvalue() {
        return DefaultValue;
    }

    public void setDefaultvalue(String DefaultValue) {
        this.DefaultValue = DefaultValue;
    }
    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
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
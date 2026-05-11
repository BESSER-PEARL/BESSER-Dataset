





import java.util.List;
import java.util.ArrayList;

public class dom_Dao extends ModelElement, Dependant {

    private String discriminator;
    private String qualifier;
    private String tableName;



    public dom_Dao(
        String discriminator,        String qualifier,        String tableName    ) {
        super(
        );
        this.discriminator = discriminator;
        this.qualifier = qualifier;
        this.tableName = tableName;
    }


    public String getDiscriminator() {
        return discriminator;
    }

    public void setDiscriminator(String discriminator) {
        this.discriminator = discriminator;
    }
    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }
    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }


}
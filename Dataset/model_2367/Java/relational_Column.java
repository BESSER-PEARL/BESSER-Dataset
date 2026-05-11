





import java.util.List;
import java.util.ArrayList;

public class relational_Column extends ModelElement {

    private String type;
    private String name;
    private boolean isPrimaryKey;
    private boolean isUnique;





    private relational_Table relational_table;




    private relational_Table relational_table;


    public relational_Column(
        String type,        String name,        boolean isPrimaryKey,        boolean isUnique    ) {
        super(
        );
        this.type = type;
        this.name = name;
        this.isPrimaryKey = isPrimaryKey;
        this.isUnique = isUnique;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsprimarykey() {
        return isPrimaryKey;
    }

    public void setIsprimarykey(boolean isPrimaryKey) {
        this.isPrimaryKey = isPrimaryKey;
    }
    public boolean getIsunique() {
        return isUnique;
    }

    public void setIsunique(boolean isUnique) {
        this.isUnique = isUnique;
    }

    public relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(relational_Table relational_table) {
        this.relational_table = relational_table;
    }
    public relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(relational_Table relational_table) {
        this.relational_table = relational_table;
    }

}






import java.util.List;
import java.util.ArrayList;

public class relational_Column extends ModelElement {

    private boolean isPrimaryKey;
    private String name;
    private boolean isUnique;
    private String type;





    private relational_Table relational_table;




    private relational_Table relational_table;


    public relational_Column(
        boolean isPrimaryKey,        String name,        boolean isUnique,        String type    ) {
        super(
        );
        this.isPrimaryKey = isPrimaryKey;
        this.name = name;
        this.isUnique = isUnique;
        this.type = type;
    }


    public boolean getIsprimarykey() {
        return isPrimaryKey;
    }

    public void setIsprimarykey(boolean isPrimaryKey) {
        this.isPrimaryKey = isPrimaryKey;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsunique() {
        return isUnique;
    }

    public void setIsunique(boolean isUnique) {
        this.isUnique = isUnique;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
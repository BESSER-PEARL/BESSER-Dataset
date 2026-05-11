





import java.util.List;
import java.util.ArrayList;

public class relational_obeo_Column extends ModelElement {

    private String type;
    private boolean isPrimaryKey;
    private boolean isUnique;
    private String name;





    private relational_obeo_Table relational_obeo_table;




    private relational_obeo_Table relational_obeo_table;


    public relational_obeo_Column(
        String type,        boolean isPrimaryKey,        boolean isUnique,        String name    ) {
        super(
        );
        this.type = type;
        this.isPrimaryKey = isPrimaryKey;
        this.isUnique = isUnique;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public relational_obeo_Table getRelational_obeo_table() {
        return relational_obeo_table;
    }

    public void setRelational_obeo_table(relational_obeo_Table relational_obeo_table) {
        this.relational_obeo_table = relational_obeo_table;
    }
    public relational_obeo_Table getRelational_obeo_table() {
        return relational_obeo_table;
    }

    public void setRelational_obeo_table(relational_obeo_Table relational_obeo_table) {
        this.relational_obeo_table = relational_obeo_table;
    }

}






import java.util.List;
import java.util.ArrayList;

public class relational_4relational2UML_Column extends ModelElement {

    private boolean isPrimaryKey;
    private boolean isUnique;
    private String type;
    private String name;



    public relational_4relational2UML_Column(
        boolean isPrimaryKey,        boolean isUnique,        String type,        String name    ) {
        super(
        );
        this.isPrimaryKey = isPrimaryKey;
        this.isUnique = isUnique;
        this.type = type;
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


}
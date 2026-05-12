





import java.util.List;
import java.util.ArrayList;

public class SQLDDL_Key extends TableElement {

    private String isUnique;
    private String name;



    public SQLDDL_Key(
        String isUnique,        String name    ) {
        super(
        );
        this.isUnique = isUnique;
        this.name = name;
    }


    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}






import java.util.List;
import java.util.ArrayList;

public class DB_ForeignKey extends DatabaseElement {

    private String isMany;



    public DB_ForeignKey(
        String isMany    ) {
        super(
        );
        this.isMany = isMany;
    }


    public String getIsmany() {
        return isMany;
    }

    public void setIsmany(String isMany) {
        this.isMany = isMany;
    }


}
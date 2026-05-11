





import java.util.List;
import java.util.ArrayList;

public class rdbmdl_TableColumn extends Column {

    private String isPrimaryKey;
    private String isForeignKey;



    public rdbmdl_TableColumn(
        String isPrimaryKey,        String isForeignKey    ) {
        super(
        );
        this.isPrimaryKey = isPrimaryKey;
        this.isForeignKey = isForeignKey;
    }


    public String getIsprimarykey() {
        return isPrimaryKey;
    }

    public void setIsprimarykey(String isPrimaryKey) {
        this.isPrimaryKey = isPrimaryKey;
    }
    public String getIsforeignkey() {
        return isForeignKey;
    }

    public void setIsforeignkey(String isForeignKey) {
        this.isForeignKey = isForeignKey;
    }


}
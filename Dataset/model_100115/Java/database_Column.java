





import java.util.List;
import java.util.ArrayList;

public class database_Column  {

    private String Type;
    private String Name;
    private boolean IsPrimaryKey;



    public database_Column(
        String Type,        String Name,        boolean IsPrimaryKey    ) {
        this.Type = Type;
        this.Name = Name;
        this.IsPrimaryKey = IsPrimaryKey;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public boolean getIsprimarykey() {
        return IsPrimaryKey;
    }

    public void setIsprimarykey(boolean IsPrimaryKey) {
        this.IsPrimaryKey = IsPrimaryKey;
    }


}
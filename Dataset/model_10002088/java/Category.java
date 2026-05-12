





import java.util.List;
import java.util.ArrayList;

public class Category  {

    private String Name;
    private String Type;
    private int Id;



    public Category(
        String Name,        String Type,        int Id    ) {
        this.Name = Name;
        this.Type = Type;
        this.Id = Id;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }


}
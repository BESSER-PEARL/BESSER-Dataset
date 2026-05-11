





import java.util.List;
import java.util.ArrayList;

public class NQC_Variable  {

    private String Name;
    private String Type;



    public NQC_Variable(
        String Name,        String Type    ) {
        this.Name = Name;
        this.Type = Type;
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


}
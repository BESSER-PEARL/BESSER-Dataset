





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_ForeignKey extends Restriction {

    private String Name;
    private String OnDelete;



    public ORDB4ORA_ForeignKey(
        String Name,        String OnDelete    ) {
        super(
        );
        this.Name = Name;
        this.OnDelete = OnDelete;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getOndelete() {
        return OnDelete;
    }

    public void setOndelete(String OnDelete) {
        this.OnDelete = OnDelete;
    }


}
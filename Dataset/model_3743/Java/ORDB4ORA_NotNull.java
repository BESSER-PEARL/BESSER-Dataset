





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_NotNull extends Restriction {

    private String Name;



    public ORDB4ORA_NotNull(
        String Name    ) {
        super(
        );
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}
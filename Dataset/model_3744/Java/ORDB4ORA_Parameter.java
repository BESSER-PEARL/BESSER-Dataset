





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_Parameter  {

    private String Name;





    private ORDB4ORA_Datatype ordb4ora_datatype;


    public ORDB4ORA_Parameter(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public ORDB4ORA_Datatype getOrdb4ora_datatype() {
        return ordb4ora_datatype;
    }

    public void setOrdb4ora_datatype(ORDB4ORA_Datatype ordb4ora_datatype) {
        this.ordb4ora_datatype = ordb4ora_datatype;
    }

}
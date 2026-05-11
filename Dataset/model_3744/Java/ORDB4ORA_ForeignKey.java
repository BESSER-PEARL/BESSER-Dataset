





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_ForeignKey extends Restriction {

    private String OnDelete;





    private ORDB4ORA_Table ordb4ora_table;


    public ORDB4ORA_ForeignKey(
        String OnDelete    ) {
        super(
        );
        this.OnDelete = OnDelete;
    }


    public String getOndelete() {
        return OnDelete;
    }

    public void setOndelete(String OnDelete) {
        this.OnDelete = OnDelete;
    }

    public ORDB4ORA_Table getOrdb4ora_table() {
        return ordb4ora_table;
    }

    public void setOrdb4ora_table(ORDB4ORA_Table ordb4ora_table) {
        this.ordb4ora_table = ordb4ora_table;
    }

}






import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_Restriction  {

    private String Name;
    private String NameColumns;





    private ORDB4ORA_Table ordb4ora_table;




    private ORDB4ORA_Table ordb4ora_table;


    public ORDB4ORA_Restriction(
        String Name,        String NameColumns    ) {
        this.Name = Name;
        this.NameColumns = NameColumns;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getNamecolumns() {
        return NameColumns;
    }

    public void setNamecolumns(String NameColumns) {
        this.NameColumns = NameColumns;
    }

    public ORDB4ORA_Table getOrdb4ora_table() {
        return ordb4ora_table;
    }

    public void setOrdb4ora_table(ORDB4ORA_Table ordb4ora_table) {
        this.ordb4ora_table = ordb4ora_table;
    }
    public ORDB4ORA_Table getOrdb4ora_table() {
        return ordb4ora_table;
    }

    public void setOrdb4ora_table(ORDB4ORA_Table ordb4ora_table) {
        this.ordb4ora_table = ordb4ora_table;
    }

}
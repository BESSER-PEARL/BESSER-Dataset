





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_Table  {

    private String Name;





    private ORDB4ORA_Column ordb4ora_column;




    private ORDB4ORA_ForeignKey ordb4ora_foreignkey;




    private List<ORDB4ORA_Column> ordb4ora_columns;


    public ORDB4ORA_Table(
        String Name    ) {
        this.Name = Name;
        this.ordb4ora_columns = new ArrayList<>();
    }

    public ORDB4ORA_Table(
        String Name        ArrayList<ORDB4ORA_Column> ordb4ora_columns    ) {
        this.Name = Name;
        this.ordb4ora_columns = ordb4ora_columns;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public ORDB4ORA_Column getOrdb4ora_column() {
        return ordb4ora_column;
    }

    public void setOrdb4ora_column(ORDB4ORA_Column ordb4ora_column) {
        this.ordb4ora_column = ordb4ora_column;
    }
    public ORDB4ORA_ForeignKey getOrdb4ora_foreignkey() {
        return ordb4ora_foreignkey;
    }

    public void setOrdb4ora_foreignkey(ORDB4ORA_ForeignKey ordb4ora_foreignkey) {
        this.ordb4ora_foreignkey = ordb4ora_foreignkey;
    }
    public List<ORDB4ORA_Column> getOrdb4ora_columns() {
        return ordb4ora_columns;
    }

    public void addOrdb4ora_column(Ordb4ora_column ordb4ora_column) {
        this.ordb4ora_columns.add(ordb4ora_column);
    }

}
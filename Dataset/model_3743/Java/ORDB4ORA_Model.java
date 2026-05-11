





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_Model  {

    private String Name;





    private List<ORDB4ORA_Table> ordb4ora_tables;




    private ORDB4ORA_Datatype ordb4ora_datatype;




    private List<ORDB4ORA_Datatype> ordb4ora_datatypes;




    private ORDB4ORA_Table ordb4ora_table;


    public ORDB4ORA_Model(
        String Name    ) {
        this.Name = Name;
        this.ordb4ora_tables = new ArrayList<>();
        this.ordb4ora_datatypes = new ArrayList<>();
    }

    public ORDB4ORA_Model(
        String Name        ArrayList<ORDB4ORA_Table> ordb4ora_tables,        ArrayList<ORDB4ORA_Datatype> ordb4ora_datatypes    ) {
        this.Name = Name;
        this.ordb4ora_tables = ordb4ora_tables;
        this.ordb4ora_datatypes = ordb4ora_datatypes;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<ORDB4ORA_Table> getOrdb4ora_tables() {
        return ordb4ora_tables;
    }

    public void addOrdb4ora_table(Ordb4ora_table ordb4ora_table) {
        this.ordb4ora_tables.add(ordb4ora_table);
    }
    public ORDB4ORA_Datatype getOrdb4ora_datatype() {
        return ordb4ora_datatype;
    }

    public void setOrdb4ora_datatype(ORDB4ORA_Datatype ordb4ora_datatype) {
        this.ordb4ora_datatype = ordb4ora_datatype;
    }
    public List<ORDB4ORA_Datatype> getOrdb4ora_datatypes() {
        return ordb4ora_datatypes;
    }

    public void addOrdb4ora_datatype(Ordb4ora_datatype ordb4ora_datatype) {
        this.ordb4ora_datatypes.add(ordb4ora_datatype);
    }
    public ORDB4ORA_Table getOrdb4ora_table() {
        return ordb4ora_table;
    }

    public void setOrdb4ora_table(ORDB4ORA_Table ordb4ora_table) {
        this.ordb4ora_table = ordb4ora_table;
    }

}
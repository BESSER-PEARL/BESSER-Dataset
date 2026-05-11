





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_Table  {

    private String Name;





    private ORDB4ORA_Model ordb4ora_model;




    private ORDB4ORA_Model ordb4ora_model;




    private List<ORDB4ORA_Column> ordb4ora_columns;




    private ORDB4ORA_Column ordb4ora_column;


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

    public ORDB4ORA_Model getOrdb4ora_model() {
        return ordb4ora_model;
    }

    public void setOrdb4ora_model(ORDB4ORA_Model ordb4ora_model) {
        this.ordb4ora_model = ordb4ora_model;
    }
    public ORDB4ORA_Model getOrdb4ora_model() {
        return ordb4ora_model;
    }

    public void setOrdb4ora_model(ORDB4ORA_Model ordb4ora_model) {
        this.ordb4ora_model = ordb4ora_model;
    }
    public List<ORDB4ORA_Column> getOrdb4ora_columns() {
        return ordb4ora_columns;
    }

    public void addOrdb4ora_column(Ordb4ora_column ordb4ora_column) {
        this.ordb4ora_columns.add(ordb4ora_column);
    }
    public ORDB4ORA_Column getOrdb4ora_column() {
        return ordb4ora_column;
    }

    public void setOrdb4ora_column(ORDB4ORA_Column ordb4ora_column) {
        this.ordb4ora_column = ordb4ora_column;
    }

}
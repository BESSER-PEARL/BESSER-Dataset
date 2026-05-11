





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_Package  {

    private String Name;





    private ORDB4ORA_Model ordb4ora_model;




    private ORDB4ORA_Model ordb4ora_model;




    private ORDB4ORA_Operation ordb4ora_operation;




    private List<ORDB4ORA_Operation> ordb4ora_operations;


    public ORDB4ORA_Package(
        String Name    ) {
        this.Name = Name;
        this.ordb4ora_operations = new ArrayList<>();
    }

    public ORDB4ORA_Package(
        String Name        ArrayList<ORDB4ORA_Operation> ordb4ora_operations    ) {
        this.Name = Name;
        this.ordb4ora_operations = ordb4ora_operations;
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
    public ORDB4ORA_Operation getOrdb4ora_operation() {
        return ordb4ora_operation;
    }

    public void setOrdb4ora_operation(ORDB4ORA_Operation ordb4ora_operation) {
        this.ordb4ora_operation = ordb4ora_operation;
    }
    public List<ORDB4ORA_Operation> getOrdb4ora_operations() {
        return ordb4ora_operations;
    }

    public void addOrdb4ora_operation(Ordb4ora_operation ordb4ora_operation) {
        this.ordb4ora_operations.add(ordb4ora_operation);
    }

}
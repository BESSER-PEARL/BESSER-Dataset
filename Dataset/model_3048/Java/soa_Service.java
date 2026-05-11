





import java.util.List;
import java.util.ArrayList;

public class soa_Service  {

    private String name;





    private soa_Module soa_module;




    private List<soa_Operation> soa_operations;


    public soa_Service(
        String name    ) {
        this.name = name;
        this.soa_operations = new ArrayList<>();
    }

    public soa_Service(
        String name        ArrayList<soa_Operation> soa_operations    ) {
        this.name = name;
        this.soa_operations = soa_operations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public soa_Module getSoa_module() {
        return soa_module;
    }

    public void setSoa_module(soa_Module soa_module) {
        this.soa_module = soa_module;
    }
    public List<soa_Operation> getSoa_operations() {
        return soa_operations;
    }

    public void addSoa_operation(Soa_operation soa_operation) {
        this.soa_operations.add(soa_operation);
    }

}
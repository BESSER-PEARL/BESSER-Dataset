





import java.util.List;
import java.util.ArrayList;

public class avm_DataSource  {

    private String Notes;





    private avm_Value avm_value;




    private List<avm_Resource> avm_resources;


    public avm_DataSource(
        String Notes    ) {
        this.Notes = Notes;
        this.avm_resources = new ArrayList<>();
    }

    public avm_DataSource(
        String Notes        ArrayList<avm_Resource> avm_resources    ) {
        this.Notes = Notes;
        this.avm_resources = avm_resources;
    }

    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
        this.Notes = Notes;
    }

    public avm_Value getAvm_value() {
        return avm_value;
    }

    public void setAvm_value(avm_Value avm_value) {
        this.avm_value = avm_value;
    }
    public List<avm_Resource> getAvm_resources() {
        return avm_resources;
    }

    public void addAvm_resource(Avm_resource avm_resource) {
        this.avm_resources.add(avm_resource);
    }

}
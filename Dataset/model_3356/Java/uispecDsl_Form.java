





import java.util.List;
import java.util.ArrayList;

public class uispecDsl_Form  {

    private String name;





    private List<uispecDsl_Field> uispecdsl_fields;


    public uispecDsl_Form(
        String name    ) {
        this.name = name;
        this.uispecdsl_fields = new ArrayList<>();
    }

    public uispecDsl_Form(
        String name        ArrayList<uispecDsl_Field> uispecdsl_fields    ) {
        this.name = name;
        this.uispecdsl_fields = uispecdsl_fields;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<uispecDsl_Field> getUispecdsl_fields() {
        return uispecdsl_fields;
    }

    public void addUispecdsl_field(Uispecdsl_field uispecdsl_field) {
        this.uispecdsl_fields.add(uispecdsl_field);
    }

}
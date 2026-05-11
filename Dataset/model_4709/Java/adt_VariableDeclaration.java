





import java.util.List;
import java.util.ArrayList;

public class adt_VariableDeclaration  {

    private String name;





    private adt_ASort adt_asort;




    private adt_ADT adt_adt;


    public adt_VariableDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adt_ASort getAdt_asort() {
        return adt_asort;
    }

    public void setAdt_asort(adt_ASort adt_asort) {
        this.adt_asort = adt_asort;
    }
    public adt_ADT getAdt_adt() {
        return adt_adt;
    }

    public void setAdt_adt(adt_ADT adt_adt) {
        this.adt_adt = adt_adt;
    }

}
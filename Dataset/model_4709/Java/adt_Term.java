





import java.util.List;
import java.util.ArrayList;

public class adt_Term extends ATerm {






    private List<adt_ATerm> adt_aterms;




    private adt_Operation adt_operation;


    public adt_Term(
    ) {
        super(
        );
        this.adt_aterms = new ArrayList<>();
    }

    public adt_Term(
        ArrayList<adt_ATerm> adt_aterms    ) {
        this.adt_aterms = adt_aterms;
    }


    public List<adt_ATerm> getAdt_aterms() {
        return adt_aterms;
    }

    public void addAdt_aterm(Adt_aterm adt_aterm) {
        this.adt_aterms.add(adt_aterm);
    }
    public adt_Operation getAdt_operation() {
        return adt_operation;
    }

    public void setAdt_operation(adt_Operation adt_operation) {
        this.adt_operation = adt_operation;
    }

}
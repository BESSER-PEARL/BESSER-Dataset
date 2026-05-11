





import java.util.List;
import java.util.ArrayList;

public class rell_Relational extends Statement {

    private String entity;





    private rell_Relational rell_relational;


    public rell_Relational(
        String entity    ) {
        super(
        );
        this.entity = entity;
    }


    public String getEntity() {
        return entity;
    }

    public void setEntity(String entity) {
        this.entity = entity;
    }

    public rell_Relational getRell_relational() {
        return rell_relational;
    }

    public void setRell_relational(rell_Relational rell_relational) {
        this.rell_relational = rell_relational;
    }

}
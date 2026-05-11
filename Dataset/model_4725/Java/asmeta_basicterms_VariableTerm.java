





import java.util.List;
import java.util.ArrayList;

public class asmeta_basicterms_VariableTerm extends BasicTerm {

    private String kind;
    private String name;



    public asmeta_basicterms_VariableTerm(
        String kind,        String name    ) {
        super(
        );
        this.kind = kind;
        this.name = name;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
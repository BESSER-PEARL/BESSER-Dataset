





import java.util.List;
import java.util.ArrayList;

public class asmeta_basicterms_VariableTerm extends BasicTerm {

    private String name;
    private String kind;



    public asmeta_basicterms_VariableTerm(
        String name,        String kind    ) {
        super(
        );
        this.name = name;
        this.kind = kind;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}
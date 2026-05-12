





import java.util.List;
import java.util.ArrayList;

public class Relational_Attribute  {

    private int multiplicity;
    private String name;
    private boolean nullable;
    private String type;





    private Relational_CandidateKey relational_candidatekey;




    private Relational_Table relational_table;




    private Relational_Domain relational_domain;


    public Relational_Attribute(
        int multiplicity,        String name,        boolean nullable,        String type    ) {
        this.multiplicity = multiplicity;
        this.name = name;
        this.nullable = nullable;
        this.type = type;
    }


    public int getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(int multiplicity) {
        this.multiplicity = multiplicity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Relational_CandidateKey getRelational_candidatekey() {
        return relational_candidatekey;
    }

    public void setRelational_candidatekey(Relational_CandidateKey relational_candidatekey) {
        this.relational_candidatekey = relational_candidatekey;
    }
    public Relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(Relational_Table relational_table) {
        this.relational_table = relational_table;
    }
    public Relational_Domain getRelational_domain() {
        return relational_domain;
    }

    public void setRelational_domain(Relational_Domain relational_domain) {
        this.relational_domain = relational_domain;
    }

}
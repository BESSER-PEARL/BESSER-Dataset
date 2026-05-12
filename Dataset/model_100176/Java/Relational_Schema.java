





import java.util.List;
import java.util.ArrayList;

public class Relational_Schema  {

    private String name;





    private List<Relational_Constraint> relational_constraints;




    private List<Relational_Domain> relational_domains;




    private List<Relational_Table> relational_tables;


    public Relational_Schema(
        String name    ) {
        this.name = name;
        this.relational_constraints = new ArrayList<>();
        this.relational_domains = new ArrayList<>();
        this.relational_tables = new ArrayList<>();
    }

    public Relational_Schema(
        String name        ArrayList<Relational_Constraint> relational_constraints,        ArrayList<Relational_Domain> relational_domains,        ArrayList<Relational_Table> relational_tables    ) {
        this.name = name;
        this.relational_constraints = relational_constraints;
        this.relational_domains = relational_domains;
        this.relational_tables = relational_tables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Relational_Constraint> getRelational_constraints() {
        return relational_constraints;
    }

    public void addRelational_constraint(Relational_constraint relational_constraint) {
        this.relational_constraints.add(relational_constraint);
    }
    public List<Relational_Domain> getRelational_domains() {
        return relational_domains;
    }

    public void addRelational_domain(Relational_domain relational_domain) {
        this.relational_domains.add(relational_domain);
    }
    public List<Relational_Table> getRelational_tables() {
        return relational_tables;
    }

    public void addRelational_table(Relational_table relational_table) {
        this.relational_tables.add(relational_table);
    }

}
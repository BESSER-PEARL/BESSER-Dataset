





import java.util.List;
import java.util.ArrayList;

public class emig_MigratorDX extends Migrator {

    private String name;





    private emig_EClass emig_eclass;




    private emig_RewritingRule emig_rewritingrule;




    private List<emig_FilterMigrator> emig_filtermigrators;


    public emig_MigratorDX(
        String name    ) {
        super(
        );
        this.name = name;
        this.emig_filtermigrators = new ArrayList<>();
    }

    public emig_MigratorDX(
        String name        ArrayList<emig_FilterMigrator> emig_filtermigrators    ) {
        this.name = name;
        this.emig_filtermigrators = emig_filtermigrators;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public emig_EClass getEmig_eclass() {
        return emig_eclass;
    }

    public void setEmig_eclass(emig_EClass emig_eclass) {
        this.emig_eclass = emig_eclass;
    }
    public emig_RewritingRule getEmig_rewritingrule() {
        return emig_rewritingrule;
    }

    public void setEmig_rewritingrule(emig_RewritingRule emig_rewritingrule) {
        this.emig_rewritingrule = emig_rewritingrule;
    }
    public List<emig_FilterMigrator> getEmig_filtermigrators() {
        return emig_filtermigrators;
    }

    public void addEmig_filtermigrator(Emig_filtermigrator emig_filtermigrator) {
        this.emig_filtermigrators.add(emig_filtermigrator);
    }

}
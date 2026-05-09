





import java.util.List;
import java.util.ArrayList;

public class emig_MigratorSX extends Migrator {






    private List<emig_FilterMigrator> emig_filtermigrators;




    private emig_EClass emig_eclass;




    private emig_RewritingRule emig_rewritingrule;




    private emig_RewritingRule emig_rewritingrule;


    public emig_MigratorSX(
    ) {
        super(
        );
        this.emig_filtermigrators = new ArrayList<>();
    }

    public emig_MigratorSX(
        ArrayList<emig_FilterMigrator> emig_filtermigrators    ) {
        this.emig_filtermigrators = emig_filtermigrators;
    }


    public List<emig_FilterMigrator> getEmig_filtermigrators() {
        return emig_filtermigrators;
    }

    public void addEmig_filtermigrator(Emig_filtermigrator emig_filtermigrator) {
        this.emig_filtermigrators.add(emig_filtermigrator);
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
    public emig_RewritingRule getEmig_rewritingrule() {
        return emig_rewritingrule;
    }

    public void setEmig_rewritingrule(emig_RewritingRule emig_rewritingrule) {
        this.emig_rewritingrule = emig_rewritingrule;
    }

}
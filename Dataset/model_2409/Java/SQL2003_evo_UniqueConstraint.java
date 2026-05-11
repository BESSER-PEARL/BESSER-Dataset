





import java.util.List;
import java.util.ArrayList;

public class SQL2003_evo_UniqueConstraint extends TableConstraint {






    private SQL2003_evo_ReferentialConstraint sql2003_evo_referentialconstraint;


    public SQL2003_evo_UniqueConstraint(
    ) {
        super(
        );
    }



    public SQL2003_evo_ReferentialConstraint getSql2003_evo_referentialconstraint() {
        return sql2003_evo_referentialconstraint;
    }

    public void setSql2003_evo_referentialconstraint(SQL2003_evo_ReferentialConstraint sql2003_evo_referentialconstraint) {
        this.sql2003_evo_referentialconstraint = sql2003_evo_referentialconstraint;
    }

}
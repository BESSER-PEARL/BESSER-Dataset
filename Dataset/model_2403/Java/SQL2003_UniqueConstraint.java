





import java.util.List;
import java.util.ArrayList;

public class SQL2003_UniqueConstraint extends TableConstraint {






    private SQL2003_ReferentialConstraint sql2003_referentialconstraint;


    public SQL2003_UniqueConstraint(
    ) {
        super(
        );
    }



    public SQL2003_ReferentialConstraint getSql2003_referentialconstraint() {
        return sql2003_referentialconstraint;
    }

    public void setSql2003_referentialconstraint(SQL2003_ReferentialConstraint sql2003_referentialconstraint) {
        this.sql2003_referentialconstraint = sql2003_referentialconstraint;
    }

}
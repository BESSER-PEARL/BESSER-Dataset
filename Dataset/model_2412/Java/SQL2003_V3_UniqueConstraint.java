





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_UniqueConstraint extends TableConstraint {






    private SQL2003_V3_ReferentialConstraint sql2003_v3_referentialconstraint;


    public SQL2003_V3_UniqueConstraint(
    ) {
        super(
        );
    }



    public SQL2003_V3_ReferentialConstraint getSql2003_v3_referentialconstraint() {
        return sql2003_v3_referentialconstraint;
    }

    public void setSql2003_v3_referentialconstraint(SQL2003_V3_ReferentialConstraint sql2003_v3_referentialconstraint) {
        this.sql2003_v3_referentialconstraint = sql2003_v3_referentialconstraint;
    }

}
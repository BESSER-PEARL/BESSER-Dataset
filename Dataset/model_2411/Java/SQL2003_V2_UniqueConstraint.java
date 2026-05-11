





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_UniqueConstraint extends TableConstraint {






    private SQL2003_V2_ReferentialConstraint sql2003_v2_referentialconstraint;


    public SQL2003_V2_UniqueConstraint(
    ) {
        super(
        );
    }



    public SQL2003_V2_ReferentialConstraint getSql2003_v2_referentialconstraint() {
        return sql2003_v2_referentialconstraint;
    }

    public void setSql2003_v2_referentialconstraint(SQL2003_V2_ReferentialConstraint sql2003_v2_referentialconstraint) {
        this.sql2003_v2_referentialconstraint = sql2003_v2_referentialconstraint;
    }

}
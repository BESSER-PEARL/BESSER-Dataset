





import java.util.List;
import java.util.ArrayList;

public class dDL_Key  {






    private dDL_Constraint ddl_constraint;




    private List<dDL_Colname> ddl_colnames;


    public dDL_Key(
    ) {
        this.ddl_colnames = new ArrayList<>();
    }

    public dDL_Key(
        ArrayList<dDL_Colname> ddl_colnames    ) {
        this.ddl_colnames = ddl_colnames;
    }


    public dDL_Constraint getDdl_constraint() {
        return ddl_constraint;
    }

    public void setDdl_constraint(dDL_Constraint ddl_constraint) {
        this.ddl_constraint = ddl_constraint;
    }
    public List<dDL_Colname> getDdl_colnames() {
        return ddl_colnames;
    }

    public void addDdl_colname(Ddl_colname ddl_colname) {
        this.ddl_colnames.add(ddl_colname);
    }

}






import java.util.List;
import java.util.ArrayList;

public class SQL2003_evo_StructuralComponent  {

    private String name;





    private SQL2003_evo_Trigger sql2003_evo_trigger;




    private SQL2003_evo_DataType sql2003_evo_datatype;




    private SQL2003_evo_Restriction sql2003_evo_restriction;




    private List<SQL2003_evo_Restriction> sql2003_evo_restrictions;




    private List<SQL2003_evo_Feature> sql2003_evo_features;


    public SQL2003_evo_StructuralComponent(
        String name    ) {
        this.name = name;
        this.sql2003_evo_restrictions = new ArrayList<>();
        this.sql2003_evo_features = new ArrayList<>();
    }

    public SQL2003_evo_StructuralComponent(
        String name        ArrayList<SQL2003_evo_Restriction> sql2003_evo_restrictions,        ArrayList<SQL2003_evo_Feature> sql2003_evo_features    ) {
        this.name = name;
        this.sql2003_evo_restrictions = sql2003_evo_restrictions;
        this.sql2003_evo_features = sql2003_evo_features;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SQL2003_evo_Trigger getSql2003_evo_trigger() {
        return sql2003_evo_trigger;
    }

    public void setSql2003_evo_trigger(SQL2003_evo_Trigger sql2003_evo_trigger) {
        this.sql2003_evo_trigger = sql2003_evo_trigger;
    }
    public SQL2003_evo_DataType getSql2003_evo_datatype() {
        return sql2003_evo_datatype;
    }

    public void setSql2003_evo_datatype(SQL2003_evo_DataType sql2003_evo_datatype) {
        this.sql2003_evo_datatype = sql2003_evo_datatype;
    }
    public SQL2003_evo_Restriction getSql2003_evo_restriction() {
        return sql2003_evo_restriction;
    }

    public void setSql2003_evo_restriction(SQL2003_evo_Restriction sql2003_evo_restriction) {
        this.sql2003_evo_restriction = sql2003_evo_restriction;
    }
    public List<SQL2003_evo_Restriction> getSql2003_evo_restrictions() {
        return sql2003_evo_restrictions;
    }

    public void addSql2003_evo_restriction(Sql2003_evo_restriction sql2003_evo_restriction) {
        this.sql2003_evo_restrictions.add(sql2003_evo_restriction);
    }
    public List<SQL2003_evo_Feature> getSql2003_evo_features() {
        return sql2003_evo_features;
    }

    public void addSql2003_evo_feature(Sql2003_evo_feature sql2003_evo_feature) {
        this.sql2003_evo_features.add(sql2003_evo_feature);
    }

}
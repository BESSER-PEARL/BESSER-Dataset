





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_StructuralComponent  {

    private String name;





    private SQL2003_V2_Restriction sql2003_v2_restriction;




    private List<SQL2003_V2_Restriction> sql2003_v2_restrictions;




    private SQL2003_V2_Trigger sql2003_v2_trigger;




    private SQL2003_V2_DataType sql2003_v2_datatype;




    private List<SQL2003_V2_Feature> sql2003_v2_features;


    public SQL2003_V2_StructuralComponent(
        String name    ) {
        this.name = name;
        this.sql2003_v2_restrictions = new ArrayList<>();
        this.sql2003_v2_features = new ArrayList<>();
    }

    public SQL2003_V2_StructuralComponent(
        String name        ArrayList<SQL2003_V2_Restriction> sql2003_v2_restrictions,        ArrayList<SQL2003_V2_Feature> sql2003_v2_features    ) {
        this.name = name;
        this.sql2003_v2_restrictions = sql2003_v2_restrictions;
        this.sql2003_v2_features = sql2003_v2_features;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SQL2003_V2_Restriction getSql2003_v2_restriction() {
        return sql2003_v2_restriction;
    }

    public void setSql2003_v2_restriction(SQL2003_V2_Restriction sql2003_v2_restriction) {
        this.sql2003_v2_restriction = sql2003_v2_restriction;
    }
    public List<SQL2003_V2_Restriction> getSql2003_v2_restrictions() {
        return sql2003_v2_restrictions;
    }

    public void addSql2003_v2_restriction(Sql2003_v2_restriction sql2003_v2_restriction) {
        this.sql2003_v2_restrictions.add(sql2003_v2_restriction);
    }
    public SQL2003_V2_Trigger getSql2003_v2_trigger() {
        return sql2003_v2_trigger;
    }

    public void setSql2003_v2_trigger(SQL2003_V2_Trigger sql2003_v2_trigger) {
        this.sql2003_v2_trigger = sql2003_v2_trigger;
    }
    public SQL2003_V2_DataType getSql2003_v2_datatype() {
        return sql2003_v2_datatype;
    }

    public void setSql2003_v2_datatype(SQL2003_V2_DataType sql2003_v2_datatype) {
        this.sql2003_v2_datatype = sql2003_v2_datatype;
    }
    public List<SQL2003_V2_Feature> getSql2003_v2_features() {
        return sql2003_v2_features;
    }

    public void addSql2003_v2_feature(Sql2003_v2_feature sql2003_v2_feature) {
        this.sql2003_v2_features.add(sql2003_v2_feature);
    }

}
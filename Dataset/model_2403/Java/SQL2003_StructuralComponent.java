





import java.util.List;
import java.util.ArrayList;

public class SQL2003_StructuralComponent  {

    private String name;





    private List<SQL2003_Restriction> sql2003_restrictions;




    private SQL2003_Restriction sql2003_restriction;




    private SQL2003_DataType sql2003_datatype;




    private List<SQL2003_Feature> sql2003_features;


    public SQL2003_StructuralComponent(
        String name    ) {
        this.name = name;
        this.sql2003_restrictions = new ArrayList<>();
        this.sql2003_features = new ArrayList<>();
    }

    public SQL2003_StructuralComponent(
        String name        ArrayList<SQL2003_Restriction> sql2003_restrictions,        ArrayList<SQL2003_Feature> sql2003_features    ) {
        this.name = name;
        this.sql2003_restrictions = sql2003_restrictions;
        this.sql2003_features = sql2003_features;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<SQL2003_Restriction> getSql2003_restrictions() {
        return sql2003_restrictions;
    }

    public void addSql2003_restriction(Sql2003_restriction sql2003_restriction) {
        this.sql2003_restrictions.add(sql2003_restriction);
    }
    public SQL2003_Restriction getSql2003_restriction() {
        return sql2003_restriction;
    }

    public void setSql2003_restriction(SQL2003_Restriction sql2003_restriction) {
        this.sql2003_restriction = sql2003_restriction;
    }
    public SQL2003_DataType getSql2003_datatype() {
        return sql2003_datatype;
    }

    public void setSql2003_datatype(SQL2003_DataType sql2003_datatype) {
        this.sql2003_datatype = sql2003_datatype;
    }
    public List<SQL2003_Feature> getSql2003_features() {
        return sql2003_features;
    }

    public void addSql2003_feature(Sql2003_feature sql2003_feature) {
        this.sql2003_features.add(sql2003_feature);
    }

}






import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_StructuralComponent  {

    private String name;





    private SQL2003_V3_Domain sql2003_v3_domain;




    private SQL2003_V3_Trigger sql2003_v3_trigger;




    private SQL2003_V3_Domain sql2003_v3_domain;




    private List<SQL2003_V3_Feature> sql2003_v3_features;




    private SQL2003_V3_DataType sql2003_v3_datatype;


    public SQL2003_V3_StructuralComponent(
        String name    ) {
        this.name = name;
        this.sql2003_v3_features = new ArrayList<>();
    }

    public SQL2003_V3_StructuralComponent(
        String name        ArrayList<SQL2003_V3_Feature> sql2003_v3_features    ) {
        this.name = name;
        this.sql2003_v3_features = sql2003_v3_features;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SQL2003_V3_Domain getSql2003_v3_domain() {
        return sql2003_v3_domain;
    }

    public void setSql2003_v3_domain(SQL2003_V3_Domain sql2003_v3_domain) {
        this.sql2003_v3_domain = sql2003_v3_domain;
    }
    public SQL2003_V3_Trigger getSql2003_v3_trigger() {
        return sql2003_v3_trigger;
    }

    public void setSql2003_v3_trigger(SQL2003_V3_Trigger sql2003_v3_trigger) {
        this.sql2003_v3_trigger = sql2003_v3_trigger;
    }
    public SQL2003_V3_Domain getSql2003_v3_domain() {
        return sql2003_v3_domain;
    }

    public void setSql2003_v3_domain(SQL2003_V3_Domain sql2003_v3_domain) {
        this.sql2003_v3_domain = sql2003_v3_domain;
    }
    public List<SQL2003_V3_Feature> getSql2003_v3_features() {
        return sql2003_v3_features;
    }

    public void addSql2003_v3_feature(Sql2003_v3_feature sql2003_v3_feature) {
        this.sql2003_v3_features.add(sql2003_v3_feature);
    }
    public SQL2003_V3_DataType getSql2003_v3_datatype() {
        return sql2003_v3_datatype;
    }

    public void setSql2003_v3_datatype(SQL2003_V3_DataType sql2003_v3_datatype) {
        this.sql2003_v3_datatype = sql2003_v3_datatype;
    }

}
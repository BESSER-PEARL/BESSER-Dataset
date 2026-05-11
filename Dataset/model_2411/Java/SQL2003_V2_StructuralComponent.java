





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_StructuralComponent  {

    private String name;





    private SQL2003_V2_Restriction sql2003_v2_restriction;




    private SQL2003_V2_Trigger sql2003_v2_trigger;




    private SQL2003_V2_Domain sql2003_v2_domain;




    private SQL2003_V2_DataType sql2003_v2_datatype;




    private SQL2003_V2_View sql2003_v2_view;




    private List<SQL2003_V2_View> sql2003_v2_views;




    private SQL2003_V2_Domain sql2003_v2_domain;




    private List<SQL2003_V2_Feature> sql2003_v2_features;




    private List<SQL2003_V2_Restriction> sql2003_v2_restrictions;


    public SQL2003_V2_StructuralComponent(
        String name    ) {
        this.name = name;
        this.sql2003_v2_views = new ArrayList<>();
        this.sql2003_v2_features = new ArrayList<>();
        this.sql2003_v2_restrictions = new ArrayList<>();
    }

    public SQL2003_V2_StructuralComponent(
        String name        ArrayList<SQL2003_V2_View> sql2003_v2_views,        ArrayList<SQL2003_V2_Feature> sql2003_v2_features,        ArrayList<SQL2003_V2_Restriction> sql2003_v2_restrictions    ) {
        this.name = name;
        this.sql2003_v2_views = sql2003_v2_views;
        this.sql2003_v2_features = sql2003_v2_features;
        this.sql2003_v2_restrictions = sql2003_v2_restrictions;
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
    public SQL2003_V2_Trigger getSql2003_v2_trigger() {
        return sql2003_v2_trigger;
    }

    public void setSql2003_v2_trigger(SQL2003_V2_Trigger sql2003_v2_trigger) {
        this.sql2003_v2_trigger = sql2003_v2_trigger;
    }
    public SQL2003_V2_Domain getSql2003_v2_domain() {
        return sql2003_v2_domain;
    }

    public void setSql2003_v2_domain(SQL2003_V2_Domain sql2003_v2_domain) {
        this.sql2003_v2_domain = sql2003_v2_domain;
    }
    public SQL2003_V2_DataType getSql2003_v2_datatype() {
        return sql2003_v2_datatype;
    }

    public void setSql2003_v2_datatype(SQL2003_V2_DataType sql2003_v2_datatype) {
        this.sql2003_v2_datatype = sql2003_v2_datatype;
    }
    public SQL2003_V2_View getSql2003_v2_view() {
        return sql2003_v2_view;
    }

    public void setSql2003_v2_view(SQL2003_V2_View sql2003_v2_view) {
        this.sql2003_v2_view = sql2003_v2_view;
    }
    public List<SQL2003_V2_View> getSql2003_v2_views() {
        return sql2003_v2_views;
    }

    public void addSql2003_v2_view(Sql2003_v2_view sql2003_v2_view) {
        this.sql2003_v2_views.add(sql2003_v2_view);
    }
    public SQL2003_V2_Domain getSql2003_v2_domain() {
        return sql2003_v2_domain;
    }

    public void setSql2003_v2_domain(SQL2003_V2_Domain sql2003_v2_domain) {
        this.sql2003_v2_domain = sql2003_v2_domain;
    }
    public List<SQL2003_V2_Feature> getSql2003_v2_features() {
        return sql2003_v2_features;
    }

    public void addSql2003_v2_feature(Sql2003_v2_feature sql2003_v2_feature) {
        this.sql2003_v2_features.add(sql2003_v2_feature);
    }
    public List<SQL2003_V2_Restriction> getSql2003_v2_restrictions() {
        return sql2003_v2_restrictions;
    }

    public void addSql2003_v2_restriction(Sql2003_v2_restriction sql2003_v2_restriction) {
        this.sql2003_v2_restrictions.add(sql2003_v2_restriction);
    }

}
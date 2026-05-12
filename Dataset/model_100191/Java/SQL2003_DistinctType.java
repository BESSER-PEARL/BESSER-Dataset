





import java.util.List;
import java.util.ArrayList;

public class SQL2003_DistinctType extends UserDefinedType {






    private SQL2003_PredefinedType sql2003_predefinedtype;




    private SQL2003_PredefinedType sql2003_predefinedtype;




    private List<SQL2003_Feature> sql2003_features;


    public SQL2003_DistinctType(
    ) {
        super(
        );
        this.sql2003_features = new ArrayList<>();
    }

    public SQL2003_DistinctType(
        ArrayList<SQL2003_Feature> sql2003_features    ) {
        this.sql2003_features = sql2003_features;
    }


    public SQL2003_PredefinedType getSql2003_predefinedtype() {
        return sql2003_predefinedtype;
    }

    public void setSql2003_predefinedtype(SQL2003_PredefinedType sql2003_predefinedtype) {
        this.sql2003_predefinedtype = sql2003_predefinedtype;
    }
    public SQL2003_PredefinedType getSql2003_predefinedtype() {
        return sql2003_predefinedtype;
    }

    public void setSql2003_predefinedtype(SQL2003_PredefinedType sql2003_predefinedtype) {
        this.sql2003_predefinedtype = sql2003_predefinedtype;
    }
    public List<SQL2003_Feature> getSql2003_features() {
        return sql2003_features;
    }

    public void addSql2003_feature(Sql2003_feature sql2003_feature) {
        this.sql2003_features.add(sql2003_feature);
    }

}
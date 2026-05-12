





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_Domain  {

    private String expression;
    private String name;
    private String default;





    private SQL2003_V2_StructuralComponent sql2003_v2_structuralcomponent;




    private SQL2003_V2_Schema sql2003_v2_schema;




    private List<SQL2003_V2_StructuralComponent> sql2003_v2_structuralcomponents;




    private SQL2003_V2_Schema sql2003_v2_schema;


    public SQL2003_V2_Domain(
        String expression,        String name,        String default    ) {
        this.expression = expression;
        this.name = name;
        this.default = default;
        this.sql2003_v2_structuralcomponents = new ArrayList<>();
    }

    public SQL2003_V2_Domain(
        String expression,        String name,        String default        ArrayList<SQL2003_V2_StructuralComponent> sql2003_v2_structuralcomponents    ) {
        this.expression = expression;
        this.name = name;
        this.default = default;
        this.sql2003_v2_structuralcomponents = sql2003_v2_structuralcomponents;
    }

    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public SQL2003_V2_StructuralComponent getSql2003_v2_structuralcomponent() {
        return sql2003_v2_structuralcomponent;
    }

    public void setSql2003_v2_structuralcomponent(SQL2003_V2_StructuralComponent sql2003_v2_structuralcomponent) {
        this.sql2003_v2_structuralcomponent = sql2003_v2_structuralcomponent;
    }
    public SQL2003_V2_Schema getSql2003_v2_schema() {
        return sql2003_v2_schema;
    }

    public void setSql2003_v2_schema(SQL2003_V2_Schema sql2003_v2_schema) {
        this.sql2003_v2_schema = sql2003_v2_schema;
    }
    public List<SQL2003_V2_StructuralComponent> getSql2003_v2_structuralcomponents() {
        return sql2003_v2_structuralcomponents;
    }

    public void addSql2003_v2_structuralcomponent(Sql2003_v2_structuralcomponent sql2003_v2_structuralcomponent) {
        this.sql2003_v2_structuralcomponents.add(sql2003_v2_structuralcomponent);
    }
    public SQL2003_V2_Schema getSql2003_v2_schema() {
        return sql2003_v2_schema;
    }

    public void setSql2003_v2_schema(SQL2003_V2_Schema sql2003_v2_schema) {
        this.sql2003_v2_schema = sql2003_v2_schema;
    }

}
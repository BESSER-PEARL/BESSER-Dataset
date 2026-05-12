





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_Restriction  {






    private SQL2003_V3_StructuralComponent sql2003_v3_structuralcomponent;




    private List<SQL2003_V3_StructuralComponent> sql2003_v3_structuralcomponents;




    private SQL2003_V3_Table sql2003_v3_table;




    private SQL2003_V3_Table sql2003_v3_table;


    public SQL2003_V3_Restriction(
    ) {
        this.sql2003_v3_structuralcomponents = new ArrayList<>();
    }

    public SQL2003_V3_Restriction(
        ArrayList<SQL2003_V3_StructuralComponent> sql2003_v3_structuralcomponents    ) {
        this.sql2003_v3_structuralcomponents = sql2003_v3_structuralcomponents;
    }


    public SQL2003_V3_StructuralComponent getSql2003_v3_structuralcomponent() {
        return sql2003_v3_structuralcomponent;
    }

    public void setSql2003_v3_structuralcomponent(SQL2003_V3_StructuralComponent sql2003_v3_structuralcomponent) {
        this.sql2003_v3_structuralcomponent = sql2003_v3_structuralcomponent;
    }
    public List<SQL2003_V3_StructuralComponent> getSql2003_v3_structuralcomponents() {
        return sql2003_v3_structuralcomponents;
    }

    public void addSql2003_v3_structuralcomponent(Sql2003_v3_structuralcomponent sql2003_v3_structuralcomponent) {
        this.sql2003_v3_structuralcomponents.add(sql2003_v3_structuralcomponent);
    }
    public SQL2003_V3_Table getSql2003_v3_table() {
        return sql2003_v3_table;
    }

    public void setSql2003_v3_table(SQL2003_V3_Table sql2003_v3_table) {
        this.sql2003_v3_table = sql2003_v3_table;
    }
    public SQL2003_V3_Table getSql2003_v3_table() {
        return sql2003_v3_table;
    }

    public void setSql2003_v3_table(SQL2003_V3_Table sql2003_v3_table) {
        this.sql2003_v3_table = sql2003_v3_table;
    }

}
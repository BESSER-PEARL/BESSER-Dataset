





import java.util.List;
import java.util.ArrayList;

public class SQL2003_evo_Restriction  {






    private SQL2003_evo_StructuralComponent sql2003_evo_structuralcomponent;




    private SQL2003_evo_Table sql2003_evo_table;




    private List<SQL2003_evo_StructuralComponent> sql2003_evo_structuralcomponents;




    private SQL2003_evo_Table sql2003_evo_table;


    public SQL2003_evo_Restriction(
    ) {
        this.sql2003_evo_structuralcomponents = new ArrayList<>();
    }

    public SQL2003_evo_Restriction(
        ArrayList<SQL2003_evo_StructuralComponent> sql2003_evo_structuralcomponents    ) {
        this.sql2003_evo_structuralcomponents = sql2003_evo_structuralcomponents;
    }


    public SQL2003_evo_StructuralComponent getSql2003_evo_structuralcomponent() {
        return sql2003_evo_structuralcomponent;
    }

    public void setSql2003_evo_structuralcomponent(SQL2003_evo_StructuralComponent sql2003_evo_structuralcomponent) {
        this.sql2003_evo_structuralcomponent = sql2003_evo_structuralcomponent;
    }
    public SQL2003_evo_Table getSql2003_evo_table() {
        return sql2003_evo_table;
    }

    public void setSql2003_evo_table(SQL2003_evo_Table sql2003_evo_table) {
        this.sql2003_evo_table = sql2003_evo_table;
    }
    public List<SQL2003_evo_StructuralComponent> getSql2003_evo_structuralcomponents() {
        return sql2003_evo_structuralcomponents;
    }

    public void addSql2003_evo_structuralcomponent(Sql2003_evo_structuralcomponent sql2003_evo_structuralcomponent) {
        this.sql2003_evo_structuralcomponents.add(sql2003_evo_structuralcomponent);
    }
    public SQL2003_evo_Table getSql2003_evo_table() {
        return sql2003_evo_table;
    }

    public void setSql2003_evo_table(SQL2003_evo_Table sql2003_evo_table) {
        this.sql2003_evo_table = sql2003_evo_table;
    }

}
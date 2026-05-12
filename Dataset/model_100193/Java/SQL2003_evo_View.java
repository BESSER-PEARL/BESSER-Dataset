





import java.util.List;
import java.util.ArrayList;

public class SQL2003_evo_View extends DerivedTable {






    private List<SQL2003_evo_StructuralComponent> sql2003_evo_structuralcomponents;




    private List<SQL2003_evo_Table> sql2003_evo_tables;




    private SQL2003_evo_Table sql2003_evo_table;




    private SQL2003_evo_StructuralComponent sql2003_evo_structuralcomponent;


    public SQL2003_evo_View(
    ) {
        super(
        );
        this.sql2003_evo_structuralcomponents = new ArrayList<>();
        this.sql2003_evo_tables = new ArrayList<>();
    }

    public SQL2003_evo_View(
        ArrayList<SQL2003_evo_StructuralComponent> sql2003_evo_structuralcomponents,        ArrayList<SQL2003_evo_Table> sql2003_evo_tables    ) {
        this.sql2003_evo_structuralcomponents = sql2003_evo_structuralcomponents;
        this.sql2003_evo_tables = sql2003_evo_tables;
    }


    public List<SQL2003_evo_StructuralComponent> getSql2003_evo_structuralcomponents() {
        return sql2003_evo_structuralcomponents;
    }

    public void addSql2003_evo_structuralcomponent(Sql2003_evo_structuralcomponent sql2003_evo_structuralcomponent) {
        this.sql2003_evo_structuralcomponents.add(sql2003_evo_structuralcomponent);
    }
    public List<SQL2003_evo_Table> getSql2003_evo_tables() {
        return sql2003_evo_tables;
    }

    public void addSql2003_evo_table(Sql2003_evo_table sql2003_evo_table) {
        this.sql2003_evo_tables.add(sql2003_evo_table);
    }
    public SQL2003_evo_Table getSql2003_evo_table() {
        return sql2003_evo_table;
    }

    public void setSql2003_evo_table(SQL2003_evo_Table sql2003_evo_table) {
        this.sql2003_evo_table = sql2003_evo_table;
    }
    public SQL2003_evo_StructuralComponent getSql2003_evo_structuralcomponent() {
        return sql2003_evo_structuralcomponent;
    }

    public void setSql2003_evo_structuralcomponent(SQL2003_evo_StructuralComponent sql2003_evo_structuralcomponent) {
        this.sql2003_evo_structuralcomponent = sql2003_evo_structuralcomponent;
    }

}
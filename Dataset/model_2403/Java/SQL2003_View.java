





import java.util.List;
import java.util.ArrayList;

public class SQL2003_View extends DerivedTable {






    private List<SQL2003_StructuralComponent> sql2003_structuralcomponents;




    private List<SQL2003_Table> sql2003_tables;




    private SQL2003_StructuralComponent sql2003_structuralcomponent;




    private SQL2003_Table sql2003_table;


    public SQL2003_View(
    ) {
        super(
        );
        this.sql2003_structuralcomponents = new ArrayList<>();
        this.sql2003_tables = new ArrayList<>();
    }

    public SQL2003_View(
        ArrayList<SQL2003_StructuralComponent> sql2003_structuralcomponents,        ArrayList<SQL2003_Table> sql2003_tables    ) {
        this.sql2003_structuralcomponents = sql2003_structuralcomponents;
        this.sql2003_tables = sql2003_tables;
    }


    public List<SQL2003_StructuralComponent> getSql2003_structuralcomponents() {
        return sql2003_structuralcomponents;
    }

    public void addSql2003_structuralcomponent(Sql2003_structuralcomponent sql2003_structuralcomponent) {
        this.sql2003_structuralcomponents.add(sql2003_structuralcomponent);
    }
    public List<SQL2003_Table> getSql2003_tables() {
        return sql2003_tables;
    }

    public void addSql2003_table(Sql2003_table sql2003_table) {
        this.sql2003_tables.add(sql2003_table);
    }
    public SQL2003_StructuralComponent getSql2003_structuralcomponent() {
        return sql2003_structuralcomponent;
    }

    public void setSql2003_structuralcomponent(SQL2003_StructuralComponent sql2003_structuralcomponent) {
        this.sql2003_structuralcomponent = sql2003_structuralcomponent;
    }
    public SQL2003_Table getSql2003_table() {
        return sql2003_table;
    }

    public void setSql2003_table(SQL2003_Table sql2003_table) {
        this.sql2003_table = sql2003_table;
    }

}
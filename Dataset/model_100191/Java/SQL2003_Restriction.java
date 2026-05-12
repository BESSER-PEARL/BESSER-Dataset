





import java.util.List;
import java.util.ArrayList;

public class SQL2003_Restriction  {

    private String NameColumns;





    private SQL2003_StructuralComponent sql2003_structuralcomponent;




    private SQL2003_Table sql2003_table;




    private SQL2003_Table sql2003_table;




    private List<SQL2003_StructuralComponent> sql2003_structuralcomponents;


    public SQL2003_Restriction(
        String NameColumns    ) {
        this.NameColumns = NameColumns;
        this.sql2003_structuralcomponents = new ArrayList<>();
    }

    public SQL2003_Restriction(
        String NameColumns        ArrayList<SQL2003_StructuralComponent> sql2003_structuralcomponents    ) {
        this.NameColumns = NameColumns;
        this.sql2003_structuralcomponents = sql2003_structuralcomponents;
    }

    public String getNamecolumns() {
        return NameColumns;
    }

    public void setNamecolumns(String NameColumns) {
        this.NameColumns = NameColumns;
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
    public SQL2003_Table getSql2003_table() {
        return sql2003_table;
    }

    public void setSql2003_table(SQL2003_Table sql2003_table) {
        this.sql2003_table = sql2003_table;
    }
    public List<SQL2003_StructuralComponent> getSql2003_structuralcomponents() {
        return sql2003_structuralcomponents;
    }

    public void addSql2003_structuralcomponent(Sql2003_structuralcomponent sql2003_structuralcomponent) {
        this.sql2003_structuralcomponents.add(sql2003_structuralcomponent);
    }

}
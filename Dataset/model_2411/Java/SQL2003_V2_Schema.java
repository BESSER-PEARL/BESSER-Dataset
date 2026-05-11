





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_Schema  {

    private String name;





    private SQL2003_V2_DataType sql2003_v2_datatype;




    private List<SQL2003_V2_Table> sql2003_v2_tables;




    private SQL2003_V2_BehaviouralComponent sql2003_v2_behaviouralcomponent;




    private SQL2003_V2_Table sql2003_v2_table;




    private List<SQL2003_V2_BehaviouralComponent> sql2003_v2_behaviouralcomponents;




    private List<SQL2003_V2_DataType> sql2003_v2_datatypes;


    public SQL2003_V2_Schema(
        String name    ) {
        this.name = name;
        this.sql2003_v2_tables = new ArrayList<>();
        this.sql2003_v2_behaviouralcomponents = new ArrayList<>();
        this.sql2003_v2_datatypes = new ArrayList<>();
    }

    public SQL2003_V2_Schema(
        String name        ArrayList<SQL2003_V2_Table> sql2003_v2_tables,        ArrayList<SQL2003_V2_BehaviouralComponent> sql2003_v2_behaviouralcomponents,        ArrayList<SQL2003_V2_DataType> sql2003_v2_datatypes    ) {
        this.name = name;
        this.sql2003_v2_tables = sql2003_v2_tables;
        this.sql2003_v2_behaviouralcomponents = sql2003_v2_behaviouralcomponents;
        this.sql2003_v2_datatypes = sql2003_v2_datatypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SQL2003_V2_DataType getSql2003_v2_datatype() {
        return sql2003_v2_datatype;
    }

    public void setSql2003_v2_datatype(SQL2003_V2_DataType sql2003_v2_datatype) {
        this.sql2003_v2_datatype = sql2003_v2_datatype;
    }
    public List<SQL2003_V2_Table> getSql2003_v2_tables() {
        return sql2003_v2_tables;
    }

    public void addSql2003_v2_table(Sql2003_v2_table sql2003_v2_table) {
        this.sql2003_v2_tables.add(sql2003_v2_table);
    }
    public SQL2003_V2_BehaviouralComponent getSql2003_v2_behaviouralcomponent() {
        return sql2003_v2_behaviouralcomponent;
    }

    public void setSql2003_v2_behaviouralcomponent(SQL2003_V2_BehaviouralComponent sql2003_v2_behaviouralcomponent) {
        this.sql2003_v2_behaviouralcomponent = sql2003_v2_behaviouralcomponent;
    }
    public SQL2003_V2_Table getSql2003_v2_table() {
        return sql2003_v2_table;
    }

    public void setSql2003_v2_table(SQL2003_V2_Table sql2003_v2_table) {
        this.sql2003_v2_table = sql2003_v2_table;
    }
    public List<SQL2003_V2_BehaviouralComponent> getSql2003_v2_behaviouralcomponents() {
        return sql2003_v2_behaviouralcomponents;
    }

    public void addSql2003_v2_behaviouralcomponent(Sql2003_v2_behaviouralcomponent sql2003_v2_behaviouralcomponent) {
        this.sql2003_v2_behaviouralcomponents.add(sql2003_v2_behaviouralcomponent);
    }
    public List<SQL2003_V2_DataType> getSql2003_v2_datatypes() {
        return sql2003_v2_datatypes;
    }

    public void addSql2003_v2_datatype(Sql2003_v2_datatype sql2003_v2_datatype) {
        this.sql2003_v2_datatypes.add(sql2003_v2_datatype);
    }

}
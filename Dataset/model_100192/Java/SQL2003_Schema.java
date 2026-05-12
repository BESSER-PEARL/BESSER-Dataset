





import java.util.List;
import java.util.ArrayList;

public class SQL2003_Schema  {

    private String name;





    private SQL2003_BehaviouralComponent sql2003_behaviouralcomponent;




    private List<SQL2003_BehaviouralComponent> sql2003_behaviouralcomponents;


    public SQL2003_Schema(
        String name    ) {
        this.name = name;
        this.sql2003_behaviouralcomponents = new ArrayList<>();
    }

    public SQL2003_Schema(
        String name        ArrayList<SQL2003_BehaviouralComponent> sql2003_behaviouralcomponents    ) {
        this.name = name;
        this.sql2003_behaviouralcomponents = sql2003_behaviouralcomponents;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SQL2003_BehaviouralComponent getSql2003_behaviouralcomponent() {
        return sql2003_behaviouralcomponent;
    }

    public void setSql2003_behaviouralcomponent(SQL2003_BehaviouralComponent sql2003_behaviouralcomponent) {
        this.sql2003_behaviouralcomponent = sql2003_behaviouralcomponent;
    }
    public List<SQL2003_BehaviouralComponent> getSql2003_behaviouralcomponents() {
        return sql2003_behaviouralcomponents;
    }

    public void addSql2003_behaviouralcomponent(Sql2003_behaviouralcomponent sql2003_behaviouralcomponent) {
        this.sql2003_behaviouralcomponents.add(sql2003_behaviouralcomponent);
    }

}
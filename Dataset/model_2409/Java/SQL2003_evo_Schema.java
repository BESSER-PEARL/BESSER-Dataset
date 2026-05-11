





import java.util.List;
import java.util.ArrayList;

public class SQL2003_evo_Schema  {

    private String name;





    private SQL2003_evo_BehaviouralComponent sql2003_evo_behaviouralcomponent;




    private List<SQL2003_evo_BehaviouralComponent> sql2003_evo_behaviouralcomponents;


    public SQL2003_evo_Schema(
        String name    ) {
        this.name = name;
        this.sql2003_evo_behaviouralcomponents = new ArrayList<>();
    }

    public SQL2003_evo_Schema(
        String name        ArrayList<SQL2003_evo_BehaviouralComponent> sql2003_evo_behaviouralcomponents    ) {
        this.name = name;
        this.sql2003_evo_behaviouralcomponents = sql2003_evo_behaviouralcomponents;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SQL2003_evo_BehaviouralComponent getSql2003_evo_behaviouralcomponent() {
        return sql2003_evo_behaviouralcomponent;
    }

    public void setSql2003_evo_behaviouralcomponent(SQL2003_evo_BehaviouralComponent sql2003_evo_behaviouralcomponent) {
        this.sql2003_evo_behaviouralcomponent = sql2003_evo_behaviouralcomponent;
    }
    public List<SQL2003_evo_BehaviouralComponent> getSql2003_evo_behaviouralcomponents() {
        return sql2003_evo_behaviouralcomponents;
    }

    public void addSql2003_evo_behaviouralcomponent(Sql2003_evo_behaviouralcomponent sql2003_evo_behaviouralcomponent) {
        this.sql2003_evo_behaviouralcomponents.add(sql2003_evo_behaviouralcomponent);
    }

}
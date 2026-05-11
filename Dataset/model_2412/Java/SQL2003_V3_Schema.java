





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_Schema  {

    private String name;





    private List<SQL2003_V3_BehaviouralComponent> sql2003_v3_behaviouralcomponents;




    private SQL2003_V3_BehaviouralComponent sql2003_v3_behaviouralcomponent;


    public SQL2003_V3_Schema(
        String name    ) {
        this.name = name;
        this.sql2003_v3_behaviouralcomponents = new ArrayList<>();
    }

    public SQL2003_V3_Schema(
        String name        ArrayList<SQL2003_V3_BehaviouralComponent> sql2003_v3_behaviouralcomponents    ) {
        this.name = name;
        this.sql2003_v3_behaviouralcomponents = sql2003_v3_behaviouralcomponents;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<SQL2003_V3_BehaviouralComponent> getSql2003_v3_behaviouralcomponents() {
        return sql2003_v3_behaviouralcomponents;
    }

    public void addSql2003_v3_behaviouralcomponent(Sql2003_v3_behaviouralcomponent sql2003_v3_behaviouralcomponent) {
        this.sql2003_v3_behaviouralcomponents.add(sql2003_v3_behaviouralcomponent);
    }
    public SQL2003_V3_BehaviouralComponent getSql2003_v3_behaviouralcomponent() {
        return sql2003_v3_behaviouralcomponent;
    }

    public void setSql2003_v3_behaviouralcomponent(SQL2003_V3_BehaviouralComponent sql2003_v3_behaviouralcomponent) {
        this.sql2003_v3_behaviouralcomponent = sql2003_v3_behaviouralcomponent;
    }

}
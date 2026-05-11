





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_BehaviouralComponent  {

    private String name;
    private String body;





    private SQL2003_V2_ParameterWithMode sql2003_v2_parameterwithmode;




    private List<SQL2003_V2_ParameterWithMode> sql2003_v2_parameterwithmodes;


    public SQL2003_V2_BehaviouralComponent(
        String name,        String body    ) {
        this.name = name;
        this.body = body;
        this.sql2003_v2_parameterwithmodes = new ArrayList<>();
    }

    public SQL2003_V2_BehaviouralComponent(
        String name,        String body        ArrayList<SQL2003_V2_ParameterWithMode> sql2003_v2_parameterwithmodes    ) {
        this.name = name;
        this.body = body;
        this.sql2003_v2_parameterwithmodes = sql2003_v2_parameterwithmodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public SQL2003_V2_ParameterWithMode getSql2003_v2_parameterwithmode() {
        return sql2003_v2_parameterwithmode;
    }

    public void setSql2003_v2_parameterwithmode(SQL2003_V2_ParameterWithMode sql2003_v2_parameterwithmode) {
        this.sql2003_v2_parameterwithmode = sql2003_v2_parameterwithmode;
    }
    public List<SQL2003_V2_ParameterWithMode> getSql2003_v2_parameterwithmodes() {
        return sql2003_v2_parameterwithmodes;
    }

    public void addSql2003_v2_parameterwithmode(Sql2003_v2_parameterwithmode sql2003_v2_parameterwithmode) {
        this.sql2003_v2_parameterwithmodes.add(sql2003_v2_parameterwithmode);
    }

}
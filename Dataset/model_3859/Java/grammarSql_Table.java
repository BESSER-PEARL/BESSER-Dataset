





import java.util.List;
import java.util.ArrayList;

public class grammarSql_Table  {

    private String name;





    private grammarSql_Model grammarsql_model;


    public grammarSql_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public grammarSql_Model getGrammarsql_model() {
        return grammarsql_model;
    }

    public void setGrammarsql_model(grammarSql_Model grammarsql_model) {
        this.grammarsql_model = grammarsql_model;
    }

}
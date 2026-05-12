





import java.util.List;
import java.util.ArrayList;

public class dbmap_FilterEntry  {

    private String expression;
    private String name;





    private dbmap_OutputTable dbmap_outputtable;


    public dbmap_FilterEntry(
        String expression,        String name    ) {
        this.expression = expression;
        this.name = name;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dbmap_OutputTable getDbmap_outputtable() {
        return dbmap_outputtable;
    }

    public void setDbmap_outputtable(dbmap_OutputTable dbmap_outputtable) {
        this.dbmap_outputtable = dbmap_outputtable;
    }

}
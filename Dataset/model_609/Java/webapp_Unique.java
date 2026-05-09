





import java.util.List;
import java.util.ArrayList;

public class webapp_Unique  {






    private webapp_Constraint webapp_constraint;




    private List<webapp_Column> webapp_columns;


    public webapp_Unique(
    ) {
        this.webapp_columns = new ArrayList<>();
    }

    public webapp_Unique(
        ArrayList<webapp_Column> webapp_columns    ) {
        this.webapp_columns = webapp_columns;
    }


    public webapp_Constraint getWebapp_constraint() {
        return webapp_constraint;
    }

    public void setWebapp_constraint(webapp_Constraint webapp_constraint) {
        this.webapp_constraint = webapp_constraint;
    }
    public List<webapp_Column> getWebapp_columns() {
        return webapp_columns;
    }

    public void addWebapp_column(Webapp_column webapp_column) {
        this.webapp_columns.add(webapp_column);
    }

}






import java.util.List;
import java.util.ArrayList;

public class metamodel_Table  {

    private String name;





    private metamodel_Database metamodel_database;


    public metamodel_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metamodel_Database getMetamodel_database() {
        return metamodel_database;
    }

    public void setMetamodel_database(metamodel_Database metamodel_database) {
        this.metamodel_database = metamodel_database;
    }

}
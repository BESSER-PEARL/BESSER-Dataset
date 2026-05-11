





import java.util.List;
import java.util.ArrayList;

public class metamodel_Model  {

    private String name;





    private metamodel_DatabaseConnection metamodel_databaseconnection;


    public metamodel_Model(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metamodel_DatabaseConnection getMetamodel_databaseconnection() {
        return metamodel_databaseconnection;
    }

    public void setMetamodel_databaseconnection(metamodel_DatabaseConnection metamodel_databaseconnection) {
        this.metamodel_databaseconnection = metamodel_databaseconnection;
    }

}
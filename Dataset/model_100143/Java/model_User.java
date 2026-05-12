





import java.util.List;
import java.util.ArrayList;

public class model_User extends NamedElement, DescribedElement, FQNamedElement {

    private String password;





    private model_Database model_database;




    private model_Schema model_schema;


    public model_User(
        String password    ) {
        super(
        );
        this.password = password;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public model_Database getModel_database() {
        return model_database;
    }

    public void setModel_database(model_Database model_database) {
        this.model_database = model_database;
    }
    public model_Schema getModel_schema() {
        return model_schema;
    }

    public void setModel_schema(model_Schema model_schema) {
        this.model_schema = model_schema;
    }

}
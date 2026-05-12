





import java.util.List;
import java.util.ArrayList;

public class rdbms_Table extends ModelElement {






    private rdbms_Database rdbms_database;


    public rdbms_Table(
    ) {
        super(
        );
    }



    public rdbms_Database getRdbms_database() {
        return rdbms_database;
    }

    public void setRdbms_database(rdbms_Database rdbms_database) {
        this.rdbms_database = rdbms_database;
    }

}
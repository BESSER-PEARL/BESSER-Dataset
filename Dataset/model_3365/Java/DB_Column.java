





import java.util.List;
import java.util.ArrayList;

public class DB_Column extends NamedElement {






    private DB_Type db_type;




    private DB_ForeignKey db_foreignkey;




    private DB_ForeignKey db_foreignkey;


    public DB_Column(
    ) {
        super(
        );
    }



    public DB_Type getDb_type() {
        return db_type;
    }

    public void setDb_type(DB_Type db_type) {
        this.db_type = db_type;
    }
    public DB_ForeignKey getDb_foreignkey() {
        return db_foreignkey;
    }

    public void setDb_foreignkey(DB_ForeignKey db_foreignkey) {
        this.db_foreignkey = db_foreignkey;
    }
    public DB_ForeignKey getDb_foreignkey() {
        return db_foreignkey;
    }

    public void setDb_foreignkey(DB_ForeignKey db_foreignkey) {
        this.db_foreignkey = db_foreignkey;
    }

}
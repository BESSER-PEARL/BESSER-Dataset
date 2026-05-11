





import java.util.List;
import java.util.ArrayList;

public class database_ForeignKey extends NamedElement {






    private List<database_ForeignKeyElement> database_foreignkeyelements;


    public database_ForeignKey(
    ) {
        super(
        );
        this.database_foreignkeyelements = new ArrayList<>();
    }

    public database_ForeignKey(
        ArrayList<database_ForeignKeyElement> database_foreignkeyelements    ) {
        this.database_foreignkeyelements = database_foreignkeyelements;
    }


    public List<database_ForeignKeyElement> getDatabase_foreignkeyelements() {
        return database_foreignkeyelements;
    }

    public void addDatabase_foreignkeyelement(Database_foreignkeyelement database_foreignkeyelement) {
        this.database_foreignkeyelements.add(database_foreignkeyelement);
    }

}
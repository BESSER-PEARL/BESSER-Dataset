





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_AbstractNodeRepresentation extends AbstractRepresentation {






    private List<migrationmodeler_Bordered> migrationmodeler_bordereds;


    public migrationmodeler_AbstractNodeRepresentation(
    ) {
        super(
        );
        this.migrationmodeler_bordereds = new ArrayList<>();
    }

    public migrationmodeler_AbstractNodeRepresentation(
        ArrayList<migrationmodeler_Bordered> migrationmodeler_bordereds    ) {
        this.migrationmodeler_bordereds = migrationmodeler_bordereds;
    }


    public List<migrationmodeler_Bordered> getMigrationmodeler_bordereds() {
        return migrationmodeler_bordereds;
    }

    public void addMigrationmodeler_bordered(Migrationmodeler_bordered migrationmodeler_bordered) {
        this.migrationmodeler_bordereds.add(migrationmodeler_bordered);
    }

}
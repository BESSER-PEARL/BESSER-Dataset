





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_ContainerRepresentation extends AbstractRepresentation {

    private boolean autoSized;





    private migrationmodeler_Container migrationmodeler_container;


    public migrationmodeler_ContainerRepresentation(
        boolean autoSized    ) {
        super(
        );
        this.autoSized = autoSized;
    }


    public boolean getAutosized() {
        return autoSized;
    }

    public void setAutosized(boolean autoSized) {
        this.autoSized = autoSized;
    }

    public migrationmodeler_Container getMigrationmodeler_container() {
        return migrationmodeler_container;
    }

    public void setMigrationmodeler_container(migrationmodeler_Container migrationmodeler_container) {
        this.migrationmodeler_container = migrationmodeler_container;
    }

}
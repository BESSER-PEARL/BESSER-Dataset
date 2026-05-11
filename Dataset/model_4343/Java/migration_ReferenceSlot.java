





import java.util.List;
import java.util.ArrayList;

public class migration_ReferenceSlot extends Slot {






    private List<migration_Instance> migration_instances;




    private migration_Instance migration_instance;


    public migration_ReferenceSlot(
    ) {
        super(
        );
        this.migration_instances = new ArrayList<>();
    }

    public migration_ReferenceSlot(
        ArrayList<migration_Instance> migration_instances    ) {
        this.migration_instances = migration_instances;
    }


    public List<migration_Instance> getMigration_instances() {
        return migration_instances;
    }

    public void addMigration_instance(Migration_instance migration_instance) {
        this.migration_instances.add(migration_instance);
    }
    public migration_Instance getMigration_instance() {
        return migration_instance;
    }

    public void setMigration_instance(migration_Instance migration_instance) {
        this.migration_instance = migration_instance;
    }

}
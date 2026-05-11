





import java.util.List;
import java.util.ArrayList;

public class migration_Type  {






    private migration_Instance migration_instance;




    private List<migration_Instance> migration_instances;




    private migration_Model migration_model;




    private migration_Model migration_model;




    private migration_EClass migration_eclass;


    public migration_Type(
    ) {
        this.migration_instances = new ArrayList<>();
    }

    public migration_Type(
        ArrayList<migration_Instance> migration_instances    ) {
        this.migration_instances = migration_instances;
    }


    public migration_Instance getMigration_instance() {
        return migration_instance;
    }

    public void setMigration_instance(migration_Instance migration_instance) {
        this.migration_instance = migration_instance;
    }
    public List<migration_Instance> getMigration_instances() {
        return migration_instances;
    }

    public void addMigration_instance(Migration_instance migration_instance) {
        this.migration_instances.add(migration_instance);
    }
    public migration_Model getMigration_model() {
        return migration_model;
    }

    public void setMigration_model(migration_Model migration_model) {
        this.migration_model = migration_model;
    }
    public migration_Model getMigration_model() {
        return migration_model;
    }

    public void setMigration_model(migration_Model migration_model) {
        this.migration_model = migration_model;
    }
    public migration_EClass getMigration_eclass() {
        return migration_eclass;
    }

    public void setMigration_eclass(migration_EClass migration_eclass) {
        this.migration_eclass = migration_eclass;
    }

}
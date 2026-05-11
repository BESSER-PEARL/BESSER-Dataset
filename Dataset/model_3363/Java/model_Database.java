





import java.util.List;
import java.util.ArrayList;

public class model_Database extends NameProvider {






    private List<View> views;




    private List<Trigger> triggers;




    private List<Index> indexs;




    private List<Table> tables;




    private model_DatabaseVersion model_databaseversion;


    public model_Database(
    ) {
        super(
        );
        this.views = new ArrayList<>();
        this.triggers = new ArrayList<>();
        this.indexs = new ArrayList<>();
        this.tables = new ArrayList<>();
    }

    public model_Database(
        ArrayList<View> views,        ArrayList<Trigger> triggers,        ArrayList<Index> indexs,        ArrayList<Table> tables    ) {
        this.views = views;
        this.triggers = triggers;
        this.indexs = indexs;
        this.tables = tables;
    }


    public List<View> getViews() {
        return views;
    }

    public void addView(View view) {
        this.views.add(view);
    }
    public List<Trigger> getTriggers() {
        return triggers;
    }

    public void addTrigger(Trigger trigger) {
        this.triggers.add(trigger);
    }
    public List<Index> getIndexs() {
        return indexs;
    }

    public void addIndex(Index index) {
        this.indexs.add(index);
    }
    public List<Table> getTables() {
        return tables;
    }

    public void addTable(Table table) {
        this.tables.add(table);
    }
    public model_DatabaseVersion getModel_databaseversion() {
        return model_databaseversion;
    }

    public void setModel_databaseversion(model_DatabaseVersion model_databaseversion) {
        this.model_databaseversion = model_databaseversion;
    }

}
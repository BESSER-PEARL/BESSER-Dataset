





import java.util.List;
import java.util.ArrayList;

public class database_TableKey extends ExtensibleModel {

    private String name;
    private String mark;
    private String type;





    private List<database_TableColumn> database_tablecolumns;




    private database_TableResourceData database_tableresourcedata;




    private List<database_ForeignKey> database_foreignkeys;


    public database_TableKey(
        String name,        String mark,        String type    ) {
        super(
        );
        this.name = name;
        this.mark = mark;
        this.type = type;
        this.database_tablecolumns = new ArrayList<>();
        this.database_foreignkeys = new ArrayList<>();
    }

    public database_TableKey(
        String name,        String mark,        String type        ArrayList<database_TableColumn> database_tablecolumns,        ArrayList<database_ForeignKey> database_foreignkeys    ) {
        this.name = name;
        this.mark = mark;
        this.type = type;
        this.database_tablecolumns = database_tablecolumns;
        this.database_foreignkeys = database_foreignkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMark() {
        return mark;
    }

    public void setMark(String mark) {
        this.mark = mark;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<database_TableColumn> getDatabase_tablecolumns() {
        return database_tablecolumns;
    }

    public void addDatabase_tablecolumn(Database_tablecolumn database_tablecolumn) {
        this.database_tablecolumns.add(database_tablecolumn);
    }
    public database_TableResourceData getDatabase_tableresourcedata() {
        return database_tableresourcedata;
    }

    public void setDatabase_tableresourcedata(database_TableResourceData database_tableresourcedata) {
        this.database_tableresourcedata = database_tableresourcedata;
    }
    public List<database_ForeignKey> getDatabase_foreignkeys() {
        return database_foreignkeys;
    }

    public void addDatabase_foreignkey(Database_foreignkey database_foreignkey) {
        this.database_foreignkeys.add(database_foreignkey);
    }

}
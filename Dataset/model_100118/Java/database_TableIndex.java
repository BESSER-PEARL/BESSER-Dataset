





import java.util.List;
import java.util.ArrayList;

public class database_TableIndex extends ExtensibleModel {

    private String mark;
    private boolean unique;
    private String name;
    private boolean cluster;





    private List<database_TableIndexColumn> database_tableindexcolumns;




    private database_TableResourceData database_tableresourcedata;


    public database_TableIndex(
        String mark,        boolean unique,        String name,        boolean cluster    ) {
        super(
        );
        this.mark = mark;
        this.unique = unique;
        this.name = name;
        this.cluster = cluster;
        this.database_tableindexcolumns = new ArrayList<>();
    }

    public database_TableIndex(
        String mark,        boolean unique,        String name,        boolean cluster        ArrayList<database_TableIndexColumn> database_tableindexcolumns    ) {
        this.mark = mark;
        this.unique = unique;
        this.name = name;
        this.cluster = cluster;
        this.database_tableindexcolumns = database_tableindexcolumns;
    }

    public String getMark() {
        return mark;
    }

    public void setMark(String mark) {
        this.mark = mark;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getCluster() {
        return cluster;
    }

    public void setCluster(boolean cluster) {
        this.cluster = cluster;
    }

    public List<database_TableIndexColumn> getDatabase_tableindexcolumns() {
        return database_tableindexcolumns;
    }

    public void addDatabase_tableindexcolumn(Database_tableindexcolumn database_tableindexcolumn) {
        this.database_tableindexcolumns.add(database_tableindexcolumn);
    }
    public database_TableResourceData getDatabase_tableresourcedata() {
        return database_tableresourcedata;
    }

    public void setDatabase_tableresourcedata(database_TableResourceData database_tableresourcedata) {
        this.database_tableresourcedata = database_tableresourcedata;
    }

}
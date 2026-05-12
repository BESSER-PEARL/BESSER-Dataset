





import java.util.List;
import java.util.ArrayList;

public class sqls_SqlMethod  {

    private String name;
    private boolean array;





    private sqls_Table sqls_table;




    private sqls_SqlLibrary sqls_sqllibrary;




    private List<sqls_Tag> sqls_tags;


    public sqls_SqlMethod(
        String name,        boolean array    ) {
        this.name = name;
        this.array = array;
        this.sqls_tags = new ArrayList<>();
    }

    public sqls_SqlMethod(
        String name,        boolean array        ArrayList<sqls_Tag> sqls_tags    ) {
        this.name = name;
        this.array = array;
        this.sqls_tags = sqls_tags;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getArray() {
        return array;
    }

    public void setArray(boolean array) {
        this.array = array;
    }

    public sqls_Table getSqls_table() {
        return sqls_table;
    }

    public void setSqls_table(sqls_Table sqls_table) {
        this.sqls_table = sqls_table;
    }
    public sqls_SqlLibrary getSqls_sqllibrary() {
        return sqls_sqllibrary;
    }

    public void setSqls_sqllibrary(sqls_SqlLibrary sqls_sqllibrary) {
        this.sqls_sqllibrary = sqls_sqllibrary;
    }
    public List<sqls_Tag> getSqls_tags() {
        return sqls_tags;
    }

    public void addSqls_tag(Sqls_tag sqls_tag) {
        this.sqls_tags.add(sqls_tag);
    }

}
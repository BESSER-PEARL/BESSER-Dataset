





import java.util.List;
import java.util.ArrayList;

public class sqls_Trigger  {

    private String time;
    private String name;





    private sqls_SqlLibrary sqls_sqllibrary;




    private List<sqls_Tag> sqls_tags;




    private sqls_Table sqls_table;


    public sqls_Trigger(
        String time,        String name    ) {
        this.time = time;
        this.name = name;
        this.sqls_tags = new ArrayList<>();
    }

    public sqls_Trigger(
        String time,        String name        ArrayList<sqls_Tag> sqls_tags    ) {
        this.time = time;
        this.name = name;
        this.sqls_tags = sqls_tags;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public sqls_Table getSqls_table() {
        return sqls_table;
    }

    public void setSqls_table(sqls_Table sqls_table) {
        this.sqls_table = sqls_table;
    }

}






import java.util.List;
import java.util.ArrayList;

public class sqls_Table  {

    private String name;





    private List<sqls_Tag> sqls_tags;




    private sqls_SqlLibrary sqls_sqllibrary;


    public sqls_Table(
        String name    ) {
        this.name = name;
        this.sqls_tags = new ArrayList<>();
    }

    public sqls_Table(
        String name        ArrayList<sqls_Tag> sqls_tags    ) {
        this.name = name;
        this.sqls_tags = sqls_tags;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<sqls_Tag> getSqls_tags() {
        return sqls_tags;
    }

    public void addSqls_tag(Sqls_tag sqls_tag) {
        this.sqls_tags.add(sqls_tag);
    }
    public sqls_SqlLibrary getSqls_sqllibrary() {
        return sqls_sqllibrary;
    }

    public void setSqls_sqllibrary(sqls_SqlLibrary sqls_sqllibrary) {
        this.sqls_sqllibrary = sqls_sqllibrary;
    }

}
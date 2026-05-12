





import java.util.List;
import java.util.ArrayList;

public class sqls_Tag  {

    private String name;





    private sqls_SqlLibrary sqls_sqllibrary;


    public sqls_Tag(
        String name    ) {
        this.name = name;
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

}
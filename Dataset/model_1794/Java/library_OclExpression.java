





import java.util.List;
import java.util.ArrayList;

public class library_OclExpression  {

    private String name;
    private String context;
    private String description;
    private String query;



    public library_OclExpression(
        String name,        String context,        String description,        String query    ) {
        this.name = name;
        this.context = context;
        this.description = description;
        this.query = query;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }


}






import java.util.List;
import java.util.ArrayList;

public class datamodel_Ensemble extends TreeNode {

    private String name;
    private String description;
    private boolean derived;
    private String query;



    public datamodel_Ensemble(
        String name,        String description,        boolean derived,        String query    ) {
        super(
        );
        this.name = name;
        this.description = description;
        this.derived = derived;
        this.query = query;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }
    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }


}
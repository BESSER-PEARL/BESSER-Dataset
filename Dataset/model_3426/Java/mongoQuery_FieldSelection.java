





import java.util.List;
import java.util.ArrayList;

public class mongoQuery_FieldSelection  {

    private String key;
    private int enabled;





    private mongoQuery_Selection mongoquery_selection;


    public mongoQuery_FieldSelection(
        String key,        int enabled    ) {
        this.key = key;
        this.enabled = enabled;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public int getEnabled() {
        return enabled;
    }

    public void setEnabled(int enabled) {
        this.enabled = enabled;
    }

    public mongoQuery_Selection getMongoquery_selection() {
        return mongoquery_selection;
    }

    public void setMongoquery_selection(mongoQuery_Selection mongoquery_selection) {
        this.mongoquery_selection = mongoquery_selection;
    }

}
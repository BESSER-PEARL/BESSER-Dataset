





import java.util.List;
import java.util.ArrayList;

public class rdbmsMM_dummy  {






    private List<rdbmsMM_Schema> rdbmsmm_schemas;


    public rdbmsMM_dummy(
    ) {
        this.rdbmsmm_schemas = new ArrayList<>();
    }

    public rdbmsMM_dummy(
        ArrayList<rdbmsMM_Schema> rdbmsmm_schemas    ) {
        this.rdbmsmm_schemas = rdbmsmm_schemas;
    }


    public List<rdbmsMM_Schema> getRdbmsmm_schemas() {
        return rdbmsmm_schemas;
    }

    public void addRdbmsmm_schema(Rdbmsmm_schema rdbmsmm_schema) {
        this.rdbmsmm_schemas.add(rdbmsmm_schema);
    }

}
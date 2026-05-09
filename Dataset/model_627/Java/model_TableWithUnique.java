





import java.util.List;
import java.util.ArrayList;

public class model_TableWithUnique  {






    private List<model_TableContent> model_tablecontents;


    public model_TableWithUnique(
    ) {
        this.model_tablecontents = new ArrayList<>();
    }

    public model_TableWithUnique(
        ArrayList<model_TableContent> model_tablecontents    ) {
        this.model_tablecontents = model_tablecontents;
    }


    public List<model_TableContent> getModel_tablecontents() {
        return model_tablecontents;
    }

    public void addModel_tablecontent(Model_tablecontent model_tablecontent) {
        this.model_tablecontents.add(model_tablecontent);
    }

}
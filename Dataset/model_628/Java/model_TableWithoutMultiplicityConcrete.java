





import java.util.List;
import java.util.ArrayList;

public class model_TableWithoutMultiplicityConcrete  {






    private List<model_TableContentWithInnerChild> model_tablecontentwithinnerchilds;


    public model_TableWithoutMultiplicityConcrete(
    ) {
        this.model_tablecontentwithinnerchilds = new ArrayList<>();
    }

    public model_TableWithoutMultiplicityConcrete(
        ArrayList<model_TableContentWithInnerChild> model_tablecontentwithinnerchilds    ) {
        this.model_tablecontentwithinnerchilds = model_tablecontentwithinnerchilds;
    }


    public List<model_TableContentWithInnerChild> getModel_tablecontentwithinnerchilds() {
        return model_tablecontentwithinnerchilds;
    }

    public void addModel_tablecontentwithinnerchild(Model_tablecontentwithinnerchild model_tablecontentwithinnerchild) {
        this.model_tablecontentwithinnerchilds.add(model_tablecontentwithinnerchild);
    }

}
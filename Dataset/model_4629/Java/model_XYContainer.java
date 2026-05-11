





import java.util.List;
import java.util.ArrayList;

public class model_XYContainer extends Container {






    private List<model_XYChild> model_xychilds;


    public model_XYContainer(
    ) {
        super(
        );
        this.model_xychilds = new ArrayList<>();
    }

    public model_XYContainer(
        ArrayList<model_XYChild> model_xychilds    ) {
        this.model_xychilds = model_xychilds;
    }


    public List<model_XYChild> getModel_xychilds() {
        return model_xychilds;
    }

    public void addModel_xychild(Model_xychild model_xychild) {
        this.model_xychilds.add(model_xychild);
    }

}
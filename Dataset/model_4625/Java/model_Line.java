





import java.util.List;
import java.util.ArrayList;

public class model_Line extends Shape {






    private List<model_Position> model_positions;


    public model_Line(
    ) {
        super(
        );
        this.model_positions = new ArrayList<>();
    }

    public model_Line(
        ArrayList<model_Position> model_positions    ) {
        this.model_positions = model_positions;
    }


    public List<model_Position> getModel_positions() {
        return model_positions;
    }

    public void addModel_position(Model_position model_position) {
        this.model_positions.add(model_position);
    }

}
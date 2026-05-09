





import java.util.List;
import java.util.ArrayList;

public class model_TableContentWithoutValidation extends TableContent {

    private String name;
    private int weight;



    public model_TableContentWithoutValidation(
        String name,        int weight    ) {
        super(
        );
        this.name = name;
        this.weight = weight;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }


}
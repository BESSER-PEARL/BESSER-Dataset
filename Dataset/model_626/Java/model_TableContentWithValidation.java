





import java.util.List;
import java.util.ArrayList;

public class model_TableContentWithValidation extends TableContent {

    private int weight;
    private String name;



    public model_TableContentWithValidation(
        int weight,        String name    ) {
        super(
        );
        this.weight = weight;
        this.name = name;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
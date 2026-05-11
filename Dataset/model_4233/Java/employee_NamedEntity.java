





import java.util.List;
import java.util.ArrayList;

public class employee_NamedEntity  {

    private int wrongFeature;
    private String name;



    public employee_NamedEntity(
        int wrongFeature,        String name    ) {
        this.wrongFeature = wrongFeature;
        this.name = name;
    }


    public int getWrongfeature() {
        return wrongFeature;
    }

    public void setWrongfeature(int wrongFeature) {
        this.wrongFeature = wrongFeature;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
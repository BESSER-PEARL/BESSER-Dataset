





import java.util.List;
import java.util.ArrayList;

public class featureModel_Proposition  {

    private String nameA;
    private String nameRest;



    public featureModel_Proposition(
        String nameA,        String nameRest    ) {
        this.nameA = nameA;
        this.nameRest = nameRest;
    }


    public String getNamea() {
        return nameA;
    }

    public void setNamea(String nameA) {
        this.nameA = nameA;
    }
    public String getNamerest() {
        return nameRest;
    }

    public void setNamerest(String nameRest) {
        this.nameRest = nameRest;
    }


}
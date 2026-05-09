





import java.util.List;
import java.util.ArrayList;

public class MARTE_Library_MARTE_DataTypes_IntegerMatrix  {






    private List<IntegerVector> integervectors;


    public MARTE_Library_MARTE_DataTypes_IntegerMatrix(
    ) {
        this.integervectors = new ArrayList<>();
    }

    public MARTE_Library_MARTE_DataTypes_IntegerMatrix(
        ArrayList<IntegerVector> integervectors    ) {
        this.integervectors = integervectors;
    }


    public List<IntegerVector> getIntegervectors() {
        return integervectors;
    }

    public void addIntegervector(Integervector integervector) {
        this.integervectors.add(integervector);
    }

}






import java.util.List;
import java.util.ArrayList;

public class data_StarRanking extends Ranking {

    private String normalizedValue;



    public data_StarRanking(
        String normalizedValue    ) {
        super(
        );
        this.normalizedValue = normalizedValue;
    }


    public String getNormalizedvalue() {
        return normalizedValue;
    }

    public void setNormalizedvalue(String normalizedValue) {
        this.normalizedValue = normalizedValue;
    }


}






import java.util.List;
import java.util.ArrayList;

public class InterCity  {

    private None builder;
    private String interCityTrain;



    public InterCity(
        None builder,        String interCityTrain    ) {
        this.builder = builder;
        this.interCityTrain = interCityTrain;
    }


    public None getBuilder() {
        return builder;
    }

    public void setBuilder(None builder) {
        this.builder = builder;
    }
    public String getIntercitytrain() {
        return interCityTrain;
    }

    public void setIntercitytrain(String interCityTrain) {
        this.interCityTrain = interCityTrain;
    }


}
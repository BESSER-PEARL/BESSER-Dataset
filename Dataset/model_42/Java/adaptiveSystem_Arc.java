





import java.util.List;
import java.util.ArrayList;

public class adaptiveSystem_Arc  {

    private int weight;





    private adaptiveSystem_OccurrenceNet adaptivesystem_occurrencenet;


    public adaptiveSystem_Arc(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public adaptiveSystem_OccurrenceNet getAdaptivesystem_occurrencenet() {
        return adaptivesystem_occurrencenet;
    }

    public void setAdaptivesystem_occurrencenet(adaptiveSystem_OccurrenceNet adaptivesystem_occurrencenet) {
        this.adaptivesystem_occurrencenet = adaptivesystem_occurrencenet;
    }

}
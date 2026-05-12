




import java.time.LocalDateTime;

import java.util.List;
import java.util.ArrayList;

public class Observation extends AssessmentElement {

    private LocalDateTime whenObserved;
    private String observer;





    private Dataset dataset;


    public Observation(
        LocalDateTime whenObserved,        String observer    ) {
        super(
            String,            name,            String,            description        );
        this.whenObserved = whenObserved;
        this.observer = observer;
    }


    public LocalDateTime getWhenobserved() {
        return whenObserved;
    }

    public void setWhenobserved(LocalDateTime whenObserved) {
        this.whenObserved = whenObserved;
    }
    public String getObserver() {
        return observer;
    }

    public void setObserver(String observer) {
        this.observer = observer;
    }

    public Dataset getDataset() {
        return dataset;
    }

    public void setDataset(Dataset dataset) {
        this.dataset = dataset;
    }

}
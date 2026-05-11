




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tracker_HerdTest extends Event {

    private int daysSinceBredEstimate;
    private boolean pregnant;
    private LocalDate bredDateEstimate;



    public tracker_HerdTest(
        int daysSinceBredEstimate,        boolean pregnant,        LocalDate bredDateEstimate    ) {
        super(
        );
        this.daysSinceBredEstimate = daysSinceBredEstimate;
        this.pregnant = pregnant;
        this.bredDateEstimate = bredDateEstimate;
    }


    public int getDayssincebredestimate() {
        return daysSinceBredEstimate;
    }

    public void setDayssincebredestimate(int daysSinceBredEstimate) {
        this.daysSinceBredEstimate = daysSinceBredEstimate;
    }
    public boolean getPregnant() {
        return pregnant;
    }

    public void setPregnant(boolean pregnant) {
        this.pregnant = pregnant;
    }
    public LocalDate getBreddateestimate() {
        return bredDateEstimate;
    }

    public void setBreddateestimate(LocalDate bredDateEstimate) {
        this.bredDateEstimate = bredDateEstimate;
    }


}
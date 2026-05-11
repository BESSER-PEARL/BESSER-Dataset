




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tracker_HerdTest extends Event {

    private boolean pregnant;
    private int daysSinceBredEstimate;
    private LocalDate bredDateEstimate;



    public tracker_HerdTest(
        boolean pregnant,        int daysSinceBredEstimate,        LocalDate bredDateEstimate    ) {
        super(
        );
        this.pregnant = pregnant;
        this.daysSinceBredEstimate = daysSinceBredEstimate;
        this.bredDateEstimate = bredDateEstimate;
    }


    public boolean getPregnant() {
        return pregnant;
    }

    public void setPregnant(boolean pregnant) {
        this.pregnant = pregnant;
    }
    public int getDayssincebredestimate() {
        return daysSinceBredEstimate;
    }

    public void setDayssincebredestimate(int daysSinceBredEstimate) {
        this.daysSinceBredEstimate = daysSinceBredEstimate;
    }
    public LocalDate getBreddateestimate() {
        return bredDateEstimate;
    }

    public void setBreddateestimate(LocalDate bredDateEstimate) {
        this.bredDateEstimate = bredDateEstimate;
    }


}
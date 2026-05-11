





import java.util.List;
import java.util.ArrayList;

public class universityextended_people_Assistant extends Person {

    private boolean isDoctoralCandidate;



    public universityextended_people_Assistant(
        boolean isDoctoralCandidate    ) {
        super(
        );
        this.isDoctoralCandidate = isDoctoralCandidate;
    }


    public boolean getIsdoctoralcandidate() {
        return isDoctoralCandidate;
    }

    public void setIsdoctoralcandidate(boolean isDoctoralCandidate) {
        this.isDoctoralCandidate = isDoctoralCandidate;
    }


}
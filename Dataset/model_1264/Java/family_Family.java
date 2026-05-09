





import java.util.List;
import java.util.ArrayList;

public class family_Family  {

    private int memberCount;
    private float averageAge;



    public family_Family(
        int memberCount,        float averageAge    ) {
        this.memberCount = memberCount;
        this.averageAge = averageAge;
    }


    public int getMembercount() {
        return memberCount;
    }

    public void setMembercount(int memberCount) {
        this.memberCount = memberCount;
    }
    public float getAverageage() {
        return averageAge;
    }

    public void setAverageage(float averageAge) {
        this.averageAge = averageAge;
    }


}
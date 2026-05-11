





import java.util.List;
import java.util.ArrayList;

public class smif_constraints_MultiplicityConstraint extends TypeConstraint {

    private String isSufficent;
    private String maximumNumber;
    private String atOnce;
    private String mininumNumber;



    public smif_constraints_MultiplicityConstraint(
        String isSufficent,        String maximumNumber,        String atOnce,        String mininumNumber    ) {
        super(
        );
        this.isSufficent = isSufficent;
        this.maximumNumber = maximumNumber;
        this.atOnce = atOnce;
        this.mininumNumber = mininumNumber;
    }


    public String getIssufficent() {
        return isSufficent;
    }

    public void setIssufficent(String isSufficent) {
        this.isSufficent = isSufficent;
    }
    public String getMaximumnumber() {
        return maximumNumber;
    }

    public void setMaximumnumber(String maximumNumber) {
        this.maximumNumber = maximumNumber;
    }
    public String getAtonce() {
        return atOnce;
    }

    public void setAtonce(String atOnce) {
        this.atOnce = atOnce;
    }
    public String getMininumnumber() {
        return mininumNumber;
    }

    public void setMininumnumber(String mininumNumber) {
        this.mininumNumber = mininumNumber;
    }


}
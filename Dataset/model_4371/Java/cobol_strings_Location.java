





import java.util.List;
import java.util.ArrayList;

public class cobol_strings_Location  {

    private String position;
    private boolean initial;





    private PrimaryOperand primaryoperand;


    public cobol_strings_Location(
        String position,        boolean initial    ) {
        this.position = position;
        this.initial = initial;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }

    public PrimaryOperand getPrimaryoperand() {
        return primaryoperand;
    }

    public void setPrimaryoperand(PrimaryOperand primaryoperand) {
        this.primaryoperand = primaryoperand;
    }

}






import java.util.List;
import java.util.ArrayList;

public class workflow_AbstractState extends Named {

    private String associatedClass;



    public workflow_AbstractState(
        String associatedClass    ) {
        super(
        );
        this.associatedClass = associatedClass;
    }


    public String getAssociatedclass() {
        return associatedClass;
    }

    public void setAssociatedclass(String associatedClass) {
        this.associatedClass = associatedClass;
    }


}
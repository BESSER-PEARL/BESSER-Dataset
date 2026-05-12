





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_routines_Parameter extends TypedElement {

    private boolean locator;
    private String mode;





    private Routine routine;


    public sqlmodel_routines_Parameter(
        boolean locator,        String mode    ) {
        super(
        );
        this.locator = locator;
        this.mode = mode;
    }


    public boolean getLocator() {
        return locator;
    }

    public void setLocator(boolean locator) {
        this.locator = locator;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public Routine getRoutine() {
        return routine;
    }

    public void setRoutine(Routine routine) {
        this.routine = routine;
    }

}
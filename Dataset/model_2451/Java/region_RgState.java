





import java.util.List;
import java.util.ArrayList;

public class region_RgState extends Named {

    private boolean isFinal;
    private String exit;
    private String entry;



    public region_RgState(
        boolean isFinal,        String exit,        String entry    ) {
        super(
        );
        this.isFinal = isFinal;
        this.exit = exit;
        this.entry = entry;
    }


    public boolean getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(boolean isFinal) {
        this.isFinal = isFinal;
    }
    public String getExit() {
        return exit;
    }

    public void setExit(String exit) {
        this.exit = exit;
    }
    public String getEntry() {
        return entry;
    }

    public void setEntry(String entry) {
        this.entry = entry;
    }


}
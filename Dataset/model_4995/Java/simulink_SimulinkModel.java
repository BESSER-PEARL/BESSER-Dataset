





import java.util.List;
import java.util.ArrayList;

public class simulink_SimulinkModel extends SubSystem {

    private String file;
    private boolean isLibrary;



    public simulink_SimulinkModel(
        String file,        boolean isLibrary    ) {
        super(
        );
        this.file = file;
        this.isLibrary = isLibrary;
    }


    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public boolean getIslibrary() {
        return isLibrary;
    }

    public void setIslibrary(boolean isLibrary) {
        this.isLibrary = isLibrary;
    }


}






import java.util.List;
import java.util.ArrayList;

public class simulink_SimulinkModel extends SimulinkElement {

    private String version;
    private String file;
    private boolean library;





    private List<simulink_Block> simulink_blocks;


    public simulink_SimulinkModel(
        String version,        String file,        boolean library    ) {
        super(
        );
        this.version = version;
        this.file = file;
        this.library = library;
        this.simulink_blocks = new ArrayList<>();
    }

    public simulink_SimulinkModel(
        String version,        String file,        boolean library        ArrayList<simulink_Block> simulink_blocks    ) {
        this.version = version;
        this.file = file;
        this.library = library;
        this.simulink_blocks = simulink_blocks;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public boolean getLibrary() {
        return library;
    }

    public void setLibrary(boolean library) {
        this.library = library;
    }

    public List<simulink_Block> getSimulink_blocks() {
        return simulink_blocks;
    }

    public void addSimulink_block(Simulink_block simulink_block) {
        this.simulink_blocks.add(simulink_block);
    }

}
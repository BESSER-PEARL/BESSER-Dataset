





import java.util.List;
import java.util.ArrayList;

public class MicrocontrollerModeling_CLanguage  {

    private boolean hasMain;
    private String filesExtension;
    private String name;





    private MicrocontrollerModeling_Microcontroller microcontrollermodeling_microcontroller;


    public MicrocontrollerModeling_CLanguage(
        boolean hasMain,        String filesExtension,        String name    ) {
        this.hasMain = hasMain;
        this.filesExtension = filesExtension;
        this.name = name;
    }


    public boolean getHasmain() {
        return hasMain;
    }

    public void setHasmain(boolean hasMain) {
        this.hasMain = hasMain;
    }
    public String getFilesextension() {
        return filesExtension;
    }

    public void setFilesextension(String filesExtension) {
        this.filesExtension = filesExtension;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MicrocontrollerModeling_Microcontroller getMicrocontrollermodeling_microcontroller() {
        return microcontrollermodeling_microcontroller;
    }

    public void setMicrocontrollermodeling_microcontroller(MicrocontrollerModeling_Microcontroller microcontrollermodeling_microcontroller) {
        this.microcontrollermodeling_microcontroller = microcontrollermodeling_microcontroller;
    }

}
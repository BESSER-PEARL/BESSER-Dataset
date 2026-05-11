





import java.util.List;
import java.util.ArrayList;

public class wsn_Resource  {

    private int flash;
    private int memory;



    public wsn_Resource(
        int flash,        int memory    ) {
        this.flash = flash;
        this.memory = memory;
    }


    public int getFlash() {
        return flash;
    }

    public void setFlash(int flash) {
        this.flash = flash;
    }
    public int getMemory() {
        return memory;
    }

    public void setMemory(int memory) {
        this.memory = memory;
    }


}
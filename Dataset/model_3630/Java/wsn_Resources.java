





import java.util.List;
import java.util.ArrayList;

public class wsn_Resources extends , PlatformElement {

    private int memory;
    private int flash;



    public wsn_Resources(
        int memory,        int flash    ) {
        super(
        );
        this.memory = memory;
        this.flash = flash;
    }


    public int getMemory() {
        return memory;
    }

    public void setMemory(int memory) {
        this.memory = memory;
    }
    public int getFlash() {
        return flash;
    }

    public void setFlash(int flash) {
        this.flash = flash;
    }


}






import java.util.List;
import java.util.ArrayList;

public class Page  {

    private boolean free;
    private None owner;
    private String attribute;





    private Memory memory;


    public Page(
        boolean free,        None owner,        String attribute    ) {
        this.free = free;
        this.owner = owner;
        this.attribute = attribute;
    }


    public boolean getFree() {
        return free;
    }

    public void setFree(boolean free) {
        this.free = free;
    }
    public None getOwner() {
        return owner;
    }

    public void setOwner(None owner) {
        this.owner = owner;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public Memory getMemory() {
        return memory;
    }

    public void setMemory(Memory memory) {
        this.memory = memory;
    }

}
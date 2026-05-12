





import java.util.List;
import java.util.ArrayList;

public class Memory  {

    private None table;
    private None memory;





    private Operating_System operating_system;


    public Memory(
        None table,        None memory    ) {
        this.table = table;
        this.memory = memory;
    }


    public None getTable() {
        return table;
    }

    public void setTable(None table) {
        this.table = table;
    }
    public None getMemory() {
        return memory;
    }

    public void setMemory(None memory) {
        this.memory = memory;
    }

    public Operating_System getOperating_system() {
        return operating_system;
    }

    public void setOperating_system(Operating_System operating_system) {
        this.operating_system = operating_system;
    }

}
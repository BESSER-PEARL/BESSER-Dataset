





import java.util.List;
import java.util.ArrayList;

public class Request  {

    private int startAddress;
    private int processID;
    private int endAddress;





    private Hard_Drive hard_drive;


    public Request(
        int startAddress,        int processID,        int endAddress    ) {
        this.startAddress = startAddress;
        this.processID = processID;
        this.endAddress = endAddress;
    }


    public int getStartaddress() {
        return startAddress;
    }

    public void setStartaddress(int startAddress) {
        this.startAddress = startAddress;
    }
    public int getProcessid() {
        return processID;
    }

    public void setProcessid(int processID) {
        this.processID = processID;
    }
    public int getEndaddress() {
        return endAddress;
    }

    public void setEndaddress(int endAddress) {
        this.endAddress = endAddress;
    }

    public Hard_Drive getHard_drive() {
        return hard_drive;
    }

    public void setHard_drive(Hard_Drive hard_drive) {
        this.hard_drive = hard_drive;
    }

}
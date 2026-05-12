





import java.util.List;
import java.util.ArrayList;

public class Request  {

    private int processID;
    private int startAddress;
    private int endAddress;





    private Hard_Drive hard_drive;


    public Request(
        int processID,        int startAddress,        int endAddress    ) {
        this.processID = processID;
        this.startAddress = startAddress;
        this.endAddress = endAddress;
    }


    public int getProcessid() {
        return processID;
    }

    public void setProcessid(int processID) {
        this.processID = processID;
    }
    public int getStartaddress() {
        return startAddress;
    }

    public void setStartaddress(int startAddress) {
        this.startAddress = startAddress;
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
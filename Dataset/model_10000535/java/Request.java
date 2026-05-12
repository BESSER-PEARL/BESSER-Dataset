





import java.util.List;
import java.util.ArrayList;

public class Request  {

    private int processID;
    private int startAddress;
    private int endAddress;



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


}
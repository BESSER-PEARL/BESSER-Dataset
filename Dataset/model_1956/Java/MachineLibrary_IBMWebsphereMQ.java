





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_IBMWebsphereMQ  {

    private int sendBuffer;
    private int receiveBuffer;
    private String sendDynamicQueName;
    private String sendQueMgrName;
    private String readDynamicQueName;
    private String sendQueName;
    private int maxDataSize;
    private String qName;
    private String readQueName;
    private String readQueMgrName;



    public MachineLibrary_IBMWebsphereMQ(
        int sendBuffer,        int receiveBuffer,        String sendDynamicQueName,        String sendQueMgrName,        String readDynamicQueName,        String sendQueName,        int maxDataSize,        String qName,        String readQueName,        String readQueMgrName    ) {
        this.sendBuffer = sendBuffer;
        this.receiveBuffer = receiveBuffer;
        this.sendDynamicQueName = sendDynamicQueName;
        this.sendQueMgrName = sendQueMgrName;
        this.readDynamicQueName = readDynamicQueName;
        this.sendQueName = sendQueName;
        this.maxDataSize = maxDataSize;
        this.qName = qName;
        this.readQueName = readQueName;
        this.readQueMgrName = readQueMgrName;
    }


    public int getSendbuffer() {
        return sendBuffer;
    }

    public void setSendbuffer(int sendBuffer) {
        this.sendBuffer = sendBuffer;
    }
    public int getReceivebuffer() {
        return receiveBuffer;
    }

    public void setReceivebuffer(int receiveBuffer) {
        this.receiveBuffer = receiveBuffer;
    }
    public String getSenddynamicquename() {
        return sendDynamicQueName;
    }

    public void setSenddynamicquename(String sendDynamicQueName) {
        this.sendDynamicQueName = sendDynamicQueName;
    }
    public String getSendquemgrname() {
        return sendQueMgrName;
    }

    public void setSendquemgrname(String sendQueMgrName) {
        this.sendQueMgrName = sendQueMgrName;
    }
    public String getReaddynamicquename() {
        return readDynamicQueName;
    }

    public void setReaddynamicquename(String readDynamicQueName) {
        this.readDynamicQueName = readDynamicQueName;
    }
    public String getSendquename() {
        return sendQueName;
    }

    public void setSendquename(String sendQueName) {
        this.sendQueName = sendQueName;
    }
    public int getMaxdatasize() {
        return maxDataSize;
    }

    public void setMaxdatasize(int maxDataSize) {
        this.maxDataSize = maxDataSize;
    }
    public String getQname() {
        return qName;
    }

    public void setQname(String qName) {
        this.qName = qName;
    }
    public String getReadquename() {
        return readQueName;
    }

    public void setReadquename(String readQueName) {
        this.readQueName = readQueName;
    }
    public String getReadquemgrname() {
        return readQueMgrName;
    }

    public void setReadquemgrname(String readQueMgrName) {
        this.readQueMgrName = readQueMgrName;
    }


}
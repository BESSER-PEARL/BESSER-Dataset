





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_TCPIP_Link  {

    private int maxDataSize;
    private String address_2;
    private String address_6;
    private String address_3;
    private int termChar;
    private String address_4;
    private int protocol;
    private int port;
    private String address_1;
    private int msgDelay;
    private int receiveBuffer;
    private int sendBuffer;
    private String address_5;





    private MachineLibrary_LinkConfig machinelibrary_linkconfig;


    public MachineLibrary_TCPIP_Link(
        int maxDataSize,        String address_2,        String address_6,        String address_3,        int termChar,        String address_4,        int protocol,        int port,        String address_1,        int msgDelay,        int receiveBuffer,        int sendBuffer,        String address_5    ) {
        this.maxDataSize = maxDataSize;
        this.address_2 = address_2;
        this.address_6 = address_6;
        this.address_3 = address_3;
        this.termChar = termChar;
        this.address_4 = address_4;
        this.protocol = protocol;
        this.port = port;
        this.address_1 = address_1;
        this.msgDelay = msgDelay;
        this.receiveBuffer = receiveBuffer;
        this.sendBuffer = sendBuffer;
        this.address_5 = address_5;
    }


    public int getMaxdatasize() {
        return maxDataSize;
    }

    public void setMaxdatasize(int maxDataSize) {
        this.maxDataSize = maxDataSize;
    }
    public String getAddress_2() {
        return address_2;
    }

    public void setAddress_2(String address_2) {
        this.address_2 = address_2;
    }
    public String getAddress_6() {
        return address_6;
    }

    public void setAddress_6(String address_6) {
        this.address_6 = address_6;
    }
    public String getAddress_3() {
        return address_3;
    }

    public void setAddress_3(String address_3) {
        this.address_3 = address_3;
    }
    public int getTermchar() {
        return termChar;
    }

    public void setTermchar(int termChar) {
        this.termChar = termChar;
    }
    public String getAddress_4() {
        return address_4;
    }

    public void setAddress_4(String address_4) {
        this.address_4 = address_4;
    }
    public int getProtocol() {
        return protocol;
    }

    public void setProtocol(int protocol) {
        this.protocol = protocol;
    }
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getAddress_1() {
        return address_1;
    }

    public void setAddress_1(String address_1) {
        this.address_1 = address_1;
    }
    public int getMsgdelay() {
        return msgDelay;
    }

    public void setMsgdelay(int msgDelay) {
        this.msgDelay = msgDelay;
    }
    public int getReceivebuffer() {
        return receiveBuffer;
    }

    public void setReceivebuffer(int receiveBuffer) {
        this.receiveBuffer = receiveBuffer;
    }
    public int getSendbuffer() {
        return sendBuffer;
    }

    public void setSendbuffer(int sendBuffer) {
        this.sendBuffer = sendBuffer;
    }
    public String getAddress_5() {
        return address_5;
    }

    public void setAddress_5(String address_5) {
        this.address_5 = address_5;
    }

    public MachineLibrary_LinkConfig getMachinelibrary_linkconfig() {
        return machinelibrary_linkconfig;
    }

    public void setMachinelibrary_linkconfig(MachineLibrary_LinkConfig machinelibrary_linkconfig) {
        this.machinelibrary_linkconfig = machinelibrary_linkconfig;
    }

}






import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_CommunicationData  {

    private String comSIDDataAddress;
    private int comErrorDataLength;
    private String comRequestDataAddress;
    private String comProgressIndDataAddress;
    private int comProgressIndDataLength;
    private String comSendDataAddress;
    private int comSendDataLength;
    private String comErrorDataAddress;
    private int comSIDDataLength;
    private int comRequestDataLength;





    private MachineLibrary_NodeConfig machinelibrary_nodeconfig;


    public MachineLibrary_CommunicationData(
        String comSIDDataAddress,        int comErrorDataLength,        String comRequestDataAddress,        String comProgressIndDataAddress,        int comProgressIndDataLength,        String comSendDataAddress,        int comSendDataLength,        String comErrorDataAddress,        int comSIDDataLength,        int comRequestDataLength    ) {
        this.comSIDDataAddress = comSIDDataAddress;
        this.comErrorDataLength = comErrorDataLength;
        this.comRequestDataAddress = comRequestDataAddress;
        this.comProgressIndDataAddress = comProgressIndDataAddress;
        this.comProgressIndDataLength = comProgressIndDataLength;
        this.comSendDataAddress = comSendDataAddress;
        this.comSendDataLength = comSendDataLength;
        this.comErrorDataAddress = comErrorDataAddress;
        this.comSIDDataLength = comSIDDataLength;
        this.comRequestDataLength = comRequestDataLength;
    }


    public String getComsiddataaddress() {
        return comSIDDataAddress;
    }

    public void setComsiddataaddress(String comSIDDataAddress) {
        this.comSIDDataAddress = comSIDDataAddress;
    }
    public int getComerrordatalength() {
        return comErrorDataLength;
    }

    public void setComerrordatalength(int comErrorDataLength) {
        this.comErrorDataLength = comErrorDataLength;
    }
    public String getComrequestdataaddress() {
        return comRequestDataAddress;
    }

    public void setComrequestdataaddress(String comRequestDataAddress) {
        this.comRequestDataAddress = comRequestDataAddress;
    }
    public String getComprogressinddataaddress() {
        return comProgressIndDataAddress;
    }

    public void setComprogressinddataaddress(String comProgressIndDataAddress) {
        this.comProgressIndDataAddress = comProgressIndDataAddress;
    }
    public int getComprogressinddatalength() {
        return comProgressIndDataLength;
    }

    public void setComprogressinddatalength(int comProgressIndDataLength) {
        this.comProgressIndDataLength = comProgressIndDataLength;
    }
    public String getComsenddataaddress() {
        return comSendDataAddress;
    }

    public void setComsenddataaddress(String comSendDataAddress) {
        this.comSendDataAddress = comSendDataAddress;
    }
    public int getComsenddatalength() {
        return comSendDataLength;
    }

    public void setComsenddatalength(int comSendDataLength) {
        this.comSendDataLength = comSendDataLength;
    }
    public String getComerrordataaddress() {
        return comErrorDataAddress;
    }

    public void setComerrordataaddress(String comErrorDataAddress) {
        this.comErrorDataAddress = comErrorDataAddress;
    }
    public int getComsiddatalength() {
        return comSIDDataLength;
    }

    public void setComsiddatalength(int comSIDDataLength) {
        this.comSIDDataLength = comSIDDataLength;
    }
    public int getComrequestdatalength() {
        return comRequestDataLength;
    }

    public void setComrequestdatalength(int comRequestDataLength) {
        this.comRequestDataLength = comRequestDataLength;
    }

    public MachineLibrary_NodeConfig getMachinelibrary_nodeconfig() {
        return machinelibrary_nodeconfig;
    }

    public void setMachinelibrary_nodeconfig(MachineLibrary_NodeConfig machinelibrary_nodeconfig) {
        this.machinelibrary_nodeconfig = machinelibrary_nodeconfig;
    }

}
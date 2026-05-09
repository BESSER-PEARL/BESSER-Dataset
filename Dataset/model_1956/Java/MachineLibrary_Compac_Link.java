





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_Compac_Link  {

    private int timeout;
    private int maxDataLength;
    private int splitLongMessage;
    private int checksum;
    private String commConfig;
    private int useNotENQ;
    private int useNotACK_NAK;
    private int bcc;
    private String params;
    private int byteCount;
    private String port;
    private int bytecountcode;
    private int checksumCode;
    private int retry;





    private MachineLibrary_LinkConfig machinelibrary_linkconfig;


    public MachineLibrary_Compac_Link(
        int timeout,        int maxDataLength,        int splitLongMessage,        int checksum,        String commConfig,        int useNotENQ,        int useNotACK_NAK,        int bcc,        String params,        int byteCount,        String port,        int bytecountcode,        int checksumCode,        int retry    ) {
        this.timeout = timeout;
        this.maxDataLength = maxDataLength;
        this.splitLongMessage = splitLongMessage;
        this.checksum = checksum;
        this.commConfig = commConfig;
        this.useNotENQ = useNotENQ;
        this.useNotACK_NAK = useNotACK_NAK;
        this.bcc = bcc;
        this.params = params;
        this.byteCount = byteCount;
        this.port = port;
        this.bytecountcode = bytecountcode;
        this.checksumCode = checksumCode;
        this.retry = retry;
    }


    public int getTimeout() {
        return timeout;
    }

    public void setTimeout(int timeout) {
        this.timeout = timeout;
    }
    public int getMaxdatalength() {
        return maxDataLength;
    }

    public void setMaxdatalength(int maxDataLength) {
        this.maxDataLength = maxDataLength;
    }
    public int getSplitlongmessage() {
        return splitLongMessage;
    }

    public void setSplitlongmessage(int splitLongMessage) {
        this.splitLongMessage = splitLongMessage;
    }
    public int getChecksum() {
        return checksum;
    }

    public void setChecksum(int checksum) {
        this.checksum = checksum;
    }
    public String getCommconfig() {
        return commConfig;
    }

    public void setCommconfig(String commConfig) {
        this.commConfig = commConfig;
    }
    public int getUsenotenq() {
        return useNotENQ;
    }

    public void setUsenotenq(int useNotENQ) {
        this.useNotENQ = useNotENQ;
    }
    public int getUsenotack_nak() {
        return useNotACK_NAK;
    }

    public void setUsenotack_nak(int useNotACK_NAK) {
        this.useNotACK_NAK = useNotACK_NAK;
    }
    public int getBcc() {
        return bcc;
    }

    public void setBcc(int bcc) {
        this.bcc = bcc;
    }
    public String getParams() {
        return params;
    }

    public void setParams(String params) {
        this.params = params;
    }
    public int getBytecount() {
        return byteCount;
    }

    public void setBytecount(int byteCount) {
        this.byteCount = byteCount;
    }
    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }
    public int getBytecountcode() {
        return bytecountcode;
    }

    public void setBytecountcode(int bytecountcode) {
        this.bytecountcode = bytecountcode;
    }
    public int getChecksumcode() {
        return checksumCode;
    }

    public void setChecksumcode(int checksumCode) {
        this.checksumCode = checksumCode;
    }
    public int getRetry() {
        return retry;
    }

    public void setRetry(int retry) {
        this.retry = retry;
    }

    public MachineLibrary_LinkConfig getMachinelibrary_linkconfig() {
        return machinelibrary_linkconfig;
    }

    public void setMachinelibrary_linkconfig(MachineLibrary_LinkConfig machinelibrary_linkconfig) {
        this.machinelibrary_linkconfig = machinelibrary_linkconfig;
    }

}
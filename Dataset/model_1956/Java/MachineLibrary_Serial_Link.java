





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_Serial_Link  {

    private String port;
    private String endChar;
    private String commConfig;
    private String maxCharDelay;
    private String startChar;
    private String bufferLenght;
    private String params;
    private int logging;





    private MachineLibrary_LinkConfig machinelibrary_linkconfig;


    public MachineLibrary_Serial_Link(
        String port,        String endChar,        String commConfig,        String maxCharDelay,        String startChar,        String bufferLenght,        String params,        int logging    ) {
        this.port = port;
        this.endChar = endChar;
        this.commConfig = commConfig;
        this.maxCharDelay = maxCharDelay;
        this.startChar = startChar;
        this.bufferLenght = bufferLenght;
        this.params = params;
        this.logging = logging;
    }


    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }
    public String getEndchar() {
        return endChar;
    }

    public void setEndchar(String endChar) {
        this.endChar = endChar;
    }
    public String getCommconfig() {
        return commConfig;
    }

    public void setCommconfig(String commConfig) {
        this.commConfig = commConfig;
    }
    public String getMaxchardelay() {
        return maxCharDelay;
    }

    public void setMaxchardelay(String maxCharDelay) {
        this.maxCharDelay = maxCharDelay;
    }
    public String getStartchar() {
        return startChar;
    }

    public void setStartchar(String startChar) {
        this.startChar = startChar;
    }
    public String getBufferlenght() {
        return bufferLenght;
    }

    public void setBufferlenght(String bufferLenght) {
        this.bufferLenght = bufferLenght;
    }
    public String getParams() {
        return params;
    }

    public void setParams(String params) {
        this.params = params;
    }
    public int getLogging() {
        return logging;
    }

    public void setLogging(int logging) {
        this.logging = logging;
    }

    public MachineLibrary_LinkConfig getMachinelibrary_linkconfig() {
        return machinelibrary_linkconfig;
    }

    public void setMachinelibrary_linkconfig(MachineLibrary_LinkConfig machinelibrary_linkconfig) {
        this.machinelibrary_linkconfig = machinelibrary_linkconfig;
    }

}






import java.util.List;
import java.util.ArrayList;

public class cbmg_State  {

    private String requestURL;
    private boolean isEndState;
    private int port;
    private String localAddr;
    private boolean isStartState;
    private String localName;



    public cbmg_State(
        String requestURL,        boolean isEndState,        int port,        String localAddr,        boolean isStartState,        String localName    ) {
        this.requestURL = requestURL;
        this.isEndState = isEndState;
        this.port = port;
        this.localAddr = localAddr;
        this.isStartState = isStartState;
        this.localName = localName;
    }


    public String getRequesturl() {
        return requestURL;
    }

    public void setRequesturl(String requestURL) {
        this.requestURL = requestURL;
    }
    public boolean getIsendstate() {
        return isEndState;
    }

    public void setIsendstate(boolean isEndState) {
        this.isEndState = isEndState;
    }
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getLocaladdr() {
        return localAddr;
    }

    public void setLocaladdr(String localAddr) {
        this.localAddr = localAddr;
    }
    public boolean getIsstartstate() {
        return isStartState;
    }

    public void setIsstartstate(boolean isStartState) {
        this.isStartState = isStartState;
    }
    public String getLocalname() {
        return localName;
    }

    public void setLocalname(String localName) {
        this.localName = localName;
    }


}






import java.util.List;
import java.util.ArrayList;

public class stateMachine_Properties  {

    private String scscfHost;
    private String applicationAddress;
    private String mediaToAddr;
    private String scscfProtocol;
    private String mediaFromAddr;
    private String mediaHost;
    private int applicationServerPort;
    private boolean setupConference;
    private String mediaURI;
    private String mediaProtocol;
    private String scscfUser;
    private String applicationServerProtocol;
    private String recordPath;
    private String applicationServerHost;
    private int mediaPort;
    private int scscfPort;



    public stateMachine_Properties(
        String scscfHost,        String applicationAddress,        String mediaToAddr,        String scscfProtocol,        String mediaFromAddr,        String mediaHost,        int applicationServerPort,        boolean setupConference,        String mediaURI,        String mediaProtocol,        String scscfUser,        String applicationServerProtocol,        String recordPath,        String applicationServerHost,        int mediaPort,        int scscfPort    ) {
        this.scscfHost = scscfHost;
        this.applicationAddress = applicationAddress;
        this.mediaToAddr = mediaToAddr;
        this.scscfProtocol = scscfProtocol;
        this.mediaFromAddr = mediaFromAddr;
        this.mediaHost = mediaHost;
        this.applicationServerPort = applicationServerPort;
        this.setupConference = setupConference;
        this.mediaURI = mediaURI;
        this.mediaProtocol = mediaProtocol;
        this.scscfUser = scscfUser;
        this.applicationServerProtocol = applicationServerProtocol;
        this.recordPath = recordPath;
        this.applicationServerHost = applicationServerHost;
        this.mediaPort = mediaPort;
        this.scscfPort = scscfPort;
    }


    public String getScscfhost() {
        return scscfHost;
    }

    public void setScscfhost(String scscfHost) {
        this.scscfHost = scscfHost;
    }
    public String getApplicationaddress() {
        return applicationAddress;
    }

    public void setApplicationaddress(String applicationAddress) {
        this.applicationAddress = applicationAddress;
    }
    public String getMediatoaddr() {
        return mediaToAddr;
    }

    public void setMediatoaddr(String mediaToAddr) {
        this.mediaToAddr = mediaToAddr;
    }
    public String getScscfprotocol() {
        return scscfProtocol;
    }

    public void setScscfprotocol(String scscfProtocol) {
        this.scscfProtocol = scscfProtocol;
    }
    public String getMediafromaddr() {
        return mediaFromAddr;
    }

    public void setMediafromaddr(String mediaFromAddr) {
        this.mediaFromAddr = mediaFromAddr;
    }
    public String getMediahost() {
        return mediaHost;
    }

    public void setMediahost(String mediaHost) {
        this.mediaHost = mediaHost;
    }
    public int getApplicationserverport() {
        return applicationServerPort;
    }

    public void setApplicationserverport(int applicationServerPort) {
        this.applicationServerPort = applicationServerPort;
    }
    public boolean getSetupconference() {
        return setupConference;
    }

    public void setSetupconference(boolean setupConference) {
        this.setupConference = setupConference;
    }
    public String getMediauri() {
        return mediaURI;
    }

    public void setMediauri(String mediaURI) {
        this.mediaURI = mediaURI;
    }
    public String getMediaprotocol() {
        return mediaProtocol;
    }

    public void setMediaprotocol(String mediaProtocol) {
        this.mediaProtocol = mediaProtocol;
    }
    public String getScscfuser() {
        return scscfUser;
    }

    public void setScscfuser(String scscfUser) {
        this.scscfUser = scscfUser;
    }
    public String getApplicationserverprotocol() {
        return applicationServerProtocol;
    }

    public void setApplicationserverprotocol(String applicationServerProtocol) {
        this.applicationServerProtocol = applicationServerProtocol;
    }
    public String getRecordpath() {
        return recordPath;
    }

    public void setRecordpath(String recordPath) {
        this.recordPath = recordPath;
    }
    public String getApplicationserverhost() {
        return applicationServerHost;
    }

    public void setApplicationserverhost(String applicationServerHost) {
        this.applicationServerHost = applicationServerHost;
    }
    public int getMediaport() {
        return mediaPort;
    }

    public void setMediaport(int mediaPort) {
        this.mediaPort = mediaPort;
    }
    public int getScscfport() {
        return scscfPort;
    }

    public void setScscfport(int scscfPort) {
        this.scscfPort = scscfPort;
    }


}
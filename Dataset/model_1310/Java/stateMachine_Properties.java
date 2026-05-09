





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Properties  {

    private String mediaHost;
    private String recordPath;
    private String mediaToAddr;
    private String scscfHost;
    private String scscfProtocol;
    private String applicationServerProtocol;
    private String mediaProtocol;
    private String mediaURI;
    private int mediaPort;
    private int scscfPort;
    private String applicationAddress;
    private String mediaFromAddr;
    private String applicationServerHost;
    private boolean setupConference;
    private String scscfUser;
    private int applicationServerPort;





    private stateMachine_StateMachine statemachine_statemachine;


    public stateMachine_Properties(
        String mediaHost,        String recordPath,        String mediaToAddr,        String scscfHost,        String scscfProtocol,        String applicationServerProtocol,        String mediaProtocol,        String mediaURI,        int mediaPort,        int scscfPort,        String applicationAddress,        String mediaFromAddr,        String applicationServerHost,        boolean setupConference,        String scscfUser,        int applicationServerPort    ) {
        this.mediaHost = mediaHost;
        this.recordPath = recordPath;
        this.mediaToAddr = mediaToAddr;
        this.scscfHost = scscfHost;
        this.scscfProtocol = scscfProtocol;
        this.applicationServerProtocol = applicationServerProtocol;
        this.mediaProtocol = mediaProtocol;
        this.mediaURI = mediaURI;
        this.mediaPort = mediaPort;
        this.scscfPort = scscfPort;
        this.applicationAddress = applicationAddress;
        this.mediaFromAddr = mediaFromAddr;
        this.applicationServerHost = applicationServerHost;
        this.setupConference = setupConference;
        this.scscfUser = scscfUser;
        this.applicationServerPort = applicationServerPort;
    }


    public String getMediahost() {
        return mediaHost;
    }

    public void setMediahost(String mediaHost) {
        this.mediaHost = mediaHost;
    }
    public String getRecordpath() {
        return recordPath;
    }

    public void setRecordpath(String recordPath) {
        this.recordPath = recordPath;
    }
    public String getMediatoaddr() {
        return mediaToAddr;
    }

    public void setMediatoaddr(String mediaToAddr) {
        this.mediaToAddr = mediaToAddr;
    }
    public String getScscfhost() {
        return scscfHost;
    }

    public void setScscfhost(String scscfHost) {
        this.scscfHost = scscfHost;
    }
    public String getScscfprotocol() {
        return scscfProtocol;
    }

    public void setScscfprotocol(String scscfProtocol) {
        this.scscfProtocol = scscfProtocol;
    }
    public String getApplicationserverprotocol() {
        return applicationServerProtocol;
    }

    public void setApplicationserverprotocol(String applicationServerProtocol) {
        this.applicationServerProtocol = applicationServerProtocol;
    }
    public String getMediaprotocol() {
        return mediaProtocol;
    }

    public void setMediaprotocol(String mediaProtocol) {
        this.mediaProtocol = mediaProtocol;
    }
    public String getMediauri() {
        return mediaURI;
    }

    public void setMediauri(String mediaURI) {
        this.mediaURI = mediaURI;
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
    public String getApplicationaddress() {
        return applicationAddress;
    }

    public void setApplicationaddress(String applicationAddress) {
        this.applicationAddress = applicationAddress;
    }
    public String getMediafromaddr() {
        return mediaFromAddr;
    }

    public void setMediafromaddr(String mediaFromAddr) {
        this.mediaFromAddr = mediaFromAddr;
    }
    public String getApplicationserverhost() {
        return applicationServerHost;
    }

    public void setApplicationserverhost(String applicationServerHost) {
        this.applicationServerHost = applicationServerHost;
    }
    public boolean getSetupconference() {
        return setupConference;
    }

    public void setSetupconference(boolean setupConference) {
        this.setupConference = setupConference;
    }
    public String getScscfuser() {
        return scscfUser;
    }

    public void setScscfuser(String scscfUser) {
        this.scscfUser = scscfUser;
    }
    public int getApplicationserverport() {
        return applicationServerPort;
    }

    public void setApplicationserverport(int applicationServerPort) {
        this.applicationServerPort = applicationServerPort;
    }

    public stateMachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(stateMachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }

}
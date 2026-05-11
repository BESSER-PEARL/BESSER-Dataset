





import java.util.List;
import java.util.ArrayList;

public class arduino_Arduino  {

    private String firmataMode;
    private String comm;
    private String ver;
    private boolean synchronizing;
    private String label;
    private String board;
    private String name;
    private String status;
    private String series;
    private String lockedPin;
    private String kind;



    public arduino_Arduino(
        String firmataMode,        String comm,        String ver,        boolean synchronizing,        String label,        String board,        String name,        String status,        String series,        String lockedPin,        String kind    ) {
        this.firmataMode = firmataMode;
        this.comm = comm;
        this.ver = ver;
        this.synchronizing = synchronizing;
        this.label = label;
        this.board = board;
        this.name = name;
        this.status = status;
        this.series = series;
        this.lockedPin = lockedPin;
        this.kind = kind;
    }


    public String getFirmatamode() {
        return firmataMode;
    }

    public void setFirmatamode(String firmataMode) {
        this.firmataMode = firmataMode;
    }
    public String getComm() {
        return comm;
    }

    public void setComm(String comm) {
        this.comm = comm;
    }
    public String getVer() {
        return ver;
    }

    public void setVer(String ver) {
        this.ver = ver;
    }
    public boolean getSynchronizing() {
        return synchronizing;
    }

    public void setSynchronizing(boolean synchronizing) {
        this.synchronizing = synchronizing;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getBoard() {
        return board;
    }

    public void setBoard(String board) {
        this.board = board;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public String getLockedpin() {
        return lockedPin;
    }

    public void setLockedpin(String lockedPin) {
        this.lockedPin = lockedPin;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}
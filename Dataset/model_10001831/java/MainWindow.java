





import java.util.List;
import java.util.ArrayList;

public class MainWindow  {

    private None _logininit;
    private String nursess;
    private String roomss;
    private None _Loginnurs;
    private String itss;
    private String doctorss;
    private None _logicdoc;
    private String UI;
    private String patientss;



    public MainWindow(
        None _logininit,        String nursess,        String roomss,        None _Loginnurs,        String itss,        String doctorss,        None _logicdoc,        String UI,        String patientss    ) {
        this._logininit = _logininit;
        this.nursess = nursess;
        this.roomss = roomss;
        this._Loginnurs = _Loginnurs;
        this.itss = itss;
        this.doctorss = doctorss;
        this._logicdoc = _logicdoc;
        this.UI = UI;
        this.patientss = patientss;
    }


    public None get_logininit() {
        return _logininit;
    }

    public void set_logininit(None _logininit) {
        this._logininit = _logininit;
    }
    public String getNursess() {
        return nursess;
    }

    public void setNursess(String nursess) {
        this.nursess = nursess;
    }
    public String getRoomss() {
        return roomss;
    }

    public void setRoomss(String roomss) {
        this.roomss = roomss;
    }
    public None get_loginnurs() {
        return _Loginnurs;
    }

    public void set_loginnurs(None _Loginnurs) {
        this._Loginnurs = _Loginnurs;
    }
    public String getItss() {
        return itss;
    }

    public void setItss(String itss) {
        this.itss = itss;
    }
    public String getDoctorss() {
        return doctorss;
    }

    public void setDoctorss(String doctorss) {
        this.doctorss = doctorss;
    }
    public None get_logicdoc() {
        return _logicdoc;
    }

    public void set_logicdoc(None _logicdoc) {
        this._logicdoc = _logicdoc;
    }
    public String getUi() {
        return UI;
    }

    public void setUi(String UI) {
        this.UI = UI;
    }
    public String getPatientss() {
        return patientss;
    }

    public void setPatientss(String patientss) {
        this.patientss = patientss;
    }


}
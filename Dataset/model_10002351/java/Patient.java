





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private None _doc;
    private String illness;
    private None _nur;
    private String id;





    private doctor doctor;


    public Patient(
        None _doc,        String illness,        None _nur,        String id    ) {
        this._doc = _doc;
        this.illness = illness;
        this._nur = _nur;
        this.id = id;
    }


    public None get_doc() {
        return _doc;
    }

    public void set_doc(None _doc) {
        this._doc = _doc;
    }
    public String getIllness() {
        return illness;
    }

    public void setIllness(String illness) {
        this.illness = illness;
    }
    public None get_nur() {
        return _nur;
    }

    public void set_nur(None _nur) {
        this._nur = _nur;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(doctor doctor) {
        this.doctor = doctor;
    }

}
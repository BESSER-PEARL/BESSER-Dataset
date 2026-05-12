





import java.util.List;
import java.util.ArrayList;

public class student  {

    private String e;
    private String _attr1;
    private String result;
    private String attribute;
    private String managestudent;
    private String _attr;



    public student(
        String e,        String _attr1,        String result,        String attribute,        String managestudent,        String _attr    ) {
        this.e = e;
        this._attr1 = _attr1;
        this.result = result;
        this.attribute = attribute;
        this.managestudent = managestudent;
        this._attr = _attr;
    }


    public String getE() {
        return e;
    }

    public void setE(String e) {
        this.e = e;
    }
    public String get_attr1() {
        return _attr1;
    }

    public void set_attr1(String _attr1) {
        this._attr1 = _attr1;
    }
    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getManagestudent() {
        return managestudent;
    }

    public void setManagestudent(String managestudent) {
        this.managestudent = managestudent;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }


}
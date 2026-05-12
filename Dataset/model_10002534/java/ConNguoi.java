





import java.util.List;
import java.util.ArrayList;

public class ConNguoi  {

    private String attribute4;
    private String attribute6;
    private String attribute;
    private String attribute5;
    private String attribute2;
    private String CMND;
    private String attribute3;



    public ConNguoi(
        String attribute4,        String attribute6,        String attribute,        String attribute5,        String attribute2,        String CMND,        String attribute3    ) {
        this.attribute4 = attribute4;
        this.attribute6 = attribute6;
        this.attribute = attribute;
        this.attribute5 = attribute5;
        this.attribute2 = attribute2;
        this.CMND = CMND;
        this.attribute3 = attribute3;
    }


    public String getAttribute4() {
        return attribute4;
    }

    public void setAttribute4(String attribute4) {
        this.attribute4 = attribute4;
    }
    public String getAttribute6() {
        return attribute6;
    }

    public void setAttribute6(String attribute6) {
        this.attribute6 = attribute6;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getAttribute5() {
        return attribute5;
    }

    public void setAttribute5(String attribute5) {
        this.attribute5 = attribute5;
    }
    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public String getCmnd() {
        return CMND;
    }

    public void setCmnd(String CMND) {
        this.CMND = CMND;
    }
    public String getAttribute3() {
        return attribute3;
    }

    public void setAttribute3(String attribute3) {
        this.attribute3 = attribute3;
    }


}
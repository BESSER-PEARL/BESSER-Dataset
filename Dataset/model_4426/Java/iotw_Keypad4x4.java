





import java.util.List;
import java.util.ArrayList;

public class iotw_Keypad4x4 extends InputDevice {

    private String nameButton6;
    private String nameButton0;
    private String nameButton9;
    private String pin6;
    private String nameButton2;
    private String pin2;
    private String nameButton5;
    private String nameButton1;
    private String nameButton7;
    private String nameButtonB;
    private String nameButton4;
    private String pin1;
    private String nameButtonD;
    private String nameButtonAsterisk;
    private String nameButtonHash;
    private String keys;
    private String nameButtonA;
    private String nameButtonC;
    private String nameButton3;
    private int cols;
    private String pin5;
    private String pin3;
    private int rows;
    private String pin8;
    private String pin7;
    private String pin4;
    private String nameButton8;



    public iotw_Keypad4x4(
        String nameButton6,        String nameButton0,        String nameButton9,        String pin6,        String nameButton2,        String pin2,        String nameButton5,        String nameButton1,        String nameButton7,        String nameButtonB,        String nameButton4,        String pin1,        String nameButtonD,        String nameButtonAsterisk,        String nameButtonHash,        String keys,        String nameButtonA,        String nameButtonC,        String nameButton3,        int cols,        String pin5,        String pin3,        int rows,        String pin8,        String pin7,        String pin4,        String nameButton8    ) {
        super(
        );
        this.nameButton6 = nameButton6;
        this.nameButton0 = nameButton0;
        this.nameButton9 = nameButton9;
        this.pin6 = pin6;
        this.nameButton2 = nameButton2;
        this.pin2 = pin2;
        this.nameButton5 = nameButton5;
        this.nameButton1 = nameButton1;
        this.nameButton7 = nameButton7;
        this.nameButtonB = nameButtonB;
        this.nameButton4 = nameButton4;
        this.pin1 = pin1;
        this.nameButtonD = nameButtonD;
        this.nameButtonAsterisk = nameButtonAsterisk;
        this.nameButtonHash = nameButtonHash;
        this.keys = keys;
        this.nameButtonA = nameButtonA;
        this.nameButtonC = nameButtonC;
        this.nameButton3 = nameButton3;
        this.cols = cols;
        this.pin5 = pin5;
        this.pin3 = pin3;
        this.rows = rows;
        this.pin8 = pin8;
        this.pin7 = pin7;
        this.pin4 = pin4;
        this.nameButton8 = nameButton8;
    }


    public String getNamebutton6() {
        return nameButton6;
    }

    public void setNamebutton6(String nameButton6) {
        this.nameButton6 = nameButton6;
    }
    public String getNamebutton0() {
        return nameButton0;
    }

    public void setNamebutton0(String nameButton0) {
        this.nameButton0 = nameButton0;
    }
    public String getNamebutton9() {
        return nameButton9;
    }

    public void setNamebutton9(String nameButton9) {
        this.nameButton9 = nameButton9;
    }
    public String getPin6() {
        return pin6;
    }

    public void setPin6(String pin6) {
        this.pin6 = pin6;
    }
    public String getNamebutton2() {
        return nameButton2;
    }

    public void setNamebutton2(String nameButton2) {
        this.nameButton2 = nameButton2;
    }
    public String getPin2() {
        return pin2;
    }

    public void setPin2(String pin2) {
        this.pin2 = pin2;
    }
    public String getNamebutton5() {
        return nameButton5;
    }

    public void setNamebutton5(String nameButton5) {
        this.nameButton5 = nameButton5;
    }
    public String getNamebutton1() {
        return nameButton1;
    }

    public void setNamebutton1(String nameButton1) {
        this.nameButton1 = nameButton1;
    }
    public String getNamebutton7() {
        return nameButton7;
    }

    public void setNamebutton7(String nameButton7) {
        this.nameButton7 = nameButton7;
    }
    public String getNamebuttonb() {
        return nameButtonB;
    }

    public void setNamebuttonb(String nameButtonB) {
        this.nameButtonB = nameButtonB;
    }
    public String getNamebutton4() {
        return nameButton4;
    }

    public void setNamebutton4(String nameButton4) {
        this.nameButton4 = nameButton4;
    }
    public String getPin1() {
        return pin1;
    }

    public void setPin1(String pin1) {
        this.pin1 = pin1;
    }
    public String getNamebuttond() {
        return nameButtonD;
    }

    public void setNamebuttond(String nameButtonD) {
        this.nameButtonD = nameButtonD;
    }
    public String getNamebuttonasterisk() {
        return nameButtonAsterisk;
    }

    public void setNamebuttonasterisk(String nameButtonAsterisk) {
        this.nameButtonAsterisk = nameButtonAsterisk;
    }
    public String getNamebuttonhash() {
        return nameButtonHash;
    }

    public void setNamebuttonhash(String nameButtonHash) {
        this.nameButtonHash = nameButtonHash;
    }
    public String getKeys() {
        return keys;
    }

    public void setKeys(String keys) {
        this.keys = keys;
    }
    public String getNamebuttona() {
        return nameButtonA;
    }

    public void setNamebuttona(String nameButtonA) {
        this.nameButtonA = nameButtonA;
    }
    public String getNamebuttonc() {
        return nameButtonC;
    }

    public void setNamebuttonc(String nameButtonC) {
        this.nameButtonC = nameButtonC;
    }
    public String getNamebutton3() {
        return nameButton3;
    }

    public void setNamebutton3(String nameButton3) {
        this.nameButton3 = nameButton3;
    }
    public int getCols() {
        return cols;
    }

    public void setCols(int cols) {
        this.cols = cols;
    }
    public String getPin5() {
        return pin5;
    }

    public void setPin5(String pin5) {
        this.pin5 = pin5;
    }
    public String getPin3() {
        return pin3;
    }

    public void setPin3(String pin3) {
        this.pin3 = pin3;
    }
    public int getRows() {
        return rows;
    }

    public void setRows(int rows) {
        this.rows = rows;
    }
    public String getPin8() {
        return pin8;
    }

    public void setPin8(String pin8) {
        this.pin8 = pin8;
    }
    public String getPin7() {
        return pin7;
    }

    public void setPin7(String pin7) {
        this.pin7 = pin7;
    }
    public String getPin4() {
        return pin4;
    }

    public void setPin4(String pin4) {
        this.pin4 = pin4;
    }
    public String getNamebutton8() {
        return nameButton8;
    }

    public void setNamebutton8(String nameButton8) {
        this.nameButton8 = nameButton8;
    }


}
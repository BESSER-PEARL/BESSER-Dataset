




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Scanner  {

    private int code_Id;
    private LocalDate code_MOB;
    private LocalDate Code_EOD;
    private float Code_amount;
    private String code_serial;
    private String code_serial1;



    public Scanner(
        int code_Id,        LocalDate code_MOB,        LocalDate Code_EOD,        float Code_amount,        String code_serial,        String code_serial1    ) {
        this.code_Id = code_Id;
        this.code_MOB = code_MOB;
        this.Code_EOD = Code_EOD;
        this.Code_amount = Code_amount;
        this.code_serial = code_serial;
        this.code_serial1 = code_serial1;
    }


    public int getCode_id() {
        return code_Id;
    }

    public void setCode_id(int code_Id) {
        this.code_Id = code_Id;
    }
    public LocalDate getCode_mob() {
        return code_MOB;
    }

    public void setCode_mob(LocalDate code_MOB) {
        this.code_MOB = code_MOB;
    }
    public LocalDate getCode_eod() {
        return Code_EOD;
    }

    public void setCode_eod(LocalDate Code_EOD) {
        this.Code_EOD = Code_EOD;
    }
    public float getCode_amount() {
        return Code_amount;
    }

    public void setCode_amount(float Code_amount) {
        this.Code_amount = Code_amount;
    }
    public String getCode_serial() {
        return code_serial;
    }

    public void setCode_serial(String code_serial) {
        this.code_serial = code_serial;
    }
    public String getCode_serial1() {
        return code_serial1;
    }

    public void setCode_serial1(String code_serial1) {
        this.code_serial1 = code_serial1;
    }


}





import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class sql_ScalarOperand extends OperandList {

    private LocalDate sotime;
    private LocalDate sodt;
    private int soint;
    private String sostr;
    private String sodbl;
    private LocalDate sodate;



    public sql_ScalarOperand(
        LocalDate sotime,        LocalDate sodt,        int soint,        String sostr,        String sodbl,        LocalDate sodate    ) {
        super(
        );
        this.sotime = sotime;
        this.sodt = sodt;
        this.soint = soint;
        this.sostr = sostr;
        this.sodbl = sodbl;
        this.sodate = sodate;
    }


    public LocalDate getSotime() {
        return sotime;
    }

    public void setSotime(LocalDate sotime) {
        this.sotime = sotime;
    }
    public LocalDate getSodt() {
        return sodt;
    }

    public void setSodt(LocalDate sodt) {
        this.sodt = sodt;
    }
    public int getSoint() {
        return soint;
    }

    public void setSoint(int soint) {
        this.soint = soint;
    }
    public String getSostr() {
        return sostr;
    }

    public void setSostr(String sostr) {
        this.sostr = sostr;
    }
    public String getSodbl() {
        return sodbl;
    }

    public void setSodbl(String sodbl) {
        this.sodbl = sodbl;
    }
    public LocalDate getSodate() {
        return sodate;
    }

    public void setSodate(LocalDate sodate) {
        this.sodate = sodate;
    }


}
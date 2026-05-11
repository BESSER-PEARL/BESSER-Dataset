




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class sql_ScalarOperand extends OperandList {

    private LocalDate sodate;
    private String sostr;
    private LocalDate sodt;
    private LocalDate sotime;
    private int soint;
    private String sodbl;





    private sql_Operand sql_operand;


    public sql_ScalarOperand(
        LocalDate sodate,        String sostr,        LocalDate sodt,        LocalDate sotime,        int soint,        String sodbl    ) {
        super(
        );
        this.sodate = sodate;
        this.sostr = sostr;
        this.sodt = sodt;
        this.sotime = sotime;
        this.soint = soint;
        this.sodbl = sodbl;
    }


    public LocalDate getSodate() {
        return sodate;
    }

    public void setSodate(LocalDate sodate) {
        this.sodate = sodate;
    }
    public String getSostr() {
        return sostr;
    }

    public void setSostr(String sostr) {
        this.sostr = sostr;
    }
    public LocalDate getSodt() {
        return sodt;
    }

    public void setSodt(LocalDate sodt) {
        this.sodt = sodt;
    }
    public LocalDate getSotime() {
        return sotime;
    }

    public void setSotime(LocalDate sotime) {
        this.sotime = sotime;
    }
    public int getSoint() {
        return soint;
    }

    public void setSoint(int soint) {
        this.soint = soint;
    }
    public String getSodbl() {
        return sodbl;
    }

    public void setSodbl(String sodbl) {
        this.sodbl = sodbl;
    }

    public sql_Operand getSql_operand() {
        return sql_operand;
    }

    public void setSql_operand(sql_Operand sql_operand) {
        this.sql_operand = sql_operand;
    }

}
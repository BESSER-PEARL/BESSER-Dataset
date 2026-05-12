




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class sql_ScalarOperand extends OperandList {

    private String sostr;
    private LocalDate sodate;
    private int soint;
    private LocalDate sodt;
    private String sodbl;
    private LocalDate sotime;





    private sql_Operand sql_operand;


    public sql_ScalarOperand(
        String sostr,        LocalDate sodate,        int soint,        LocalDate sodt,        String sodbl,        LocalDate sotime    ) {
        super(
        );
        this.sostr = sostr;
        this.sodate = sodate;
        this.soint = soint;
        this.sodt = sodt;
        this.sodbl = sodbl;
        this.sotime = sotime;
    }


    public String getSostr() {
        return sostr;
    }

    public void setSostr(String sostr) {
        this.sostr = sostr;
    }
    public LocalDate getSodate() {
        return sodate;
    }

    public void setSodate(LocalDate sodate) {
        this.sodate = sodate;
    }
    public int getSoint() {
        return soint;
    }

    public void setSoint(int soint) {
        this.soint = soint;
    }
    public LocalDate getSodt() {
        return sodt;
    }

    public void setSodt(LocalDate sodt) {
        this.sodt = sodt;
    }
    public String getSodbl() {
        return sodbl;
    }

    public void setSodbl(String sodbl) {
        this.sodbl = sodbl;
    }
    public LocalDate getSotime() {
        return sotime;
    }

    public void setSotime(LocalDate sotime) {
        this.sotime = sotime;
    }

    public sql_Operand getSql_operand() {
        return sql_operand;
    }

    public void setSql_operand(sql_Operand sql_operand) {
        this.sql_operand = sql_operand;
    }

}
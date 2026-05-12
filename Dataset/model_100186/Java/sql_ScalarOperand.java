




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class sql_ScalarOperand extends OperandList {

    private int soint;
    private LocalDate sodate;
    private LocalDate sotime;
    private String sodbl;
    private String sostr;
    private LocalDate sodt;





    private sql_Operand sql_operand;


    public sql_ScalarOperand(
        int soint,        LocalDate sodate,        LocalDate sotime,        String sodbl,        String sostr,        LocalDate sodt    ) {
        super(
        );
        this.soint = soint;
        this.sodate = sodate;
        this.sotime = sotime;
        this.sodbl = sodbl;
        this.sostr = sostr;
        this.sodt = sodt;
    }


    public int getSoint() {
        return soint;
    }

    public void setSoint(int soint) {
        this.soint = soint;
    }
    public LocalDate getSodate() {
        return sodate;
    }

    public void setSodate(LocalDate sodate) {
        this.sodate = sodate;
    }
    public LocalDate getSotime() {
        return sotime;
    }

    public void setSotime(LocalDate sotime) {
        this.sotime = sotime;
    }
    public String getSodbl() {
        return sodbl;
    }

    public void setSodbl(String sodbl) {
        this.sodbl = sodbl;
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

    public sql_Operand getSql_operand() {
        return sql_operand;
    }

    public void setSql_operand(sql_Operand sql_operand) {
        this.sql_operand = sql_operand;
    }

}